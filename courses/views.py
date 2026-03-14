from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  # 新增导入
from django.contrib.auth.decorators import login_required  # 限制必须登录才能选课
from .models import Course, Enrollment, Assignment, StudentSubmission, Comment
from django.contrib.auth.models import User  # 导入用户模型
from django.contrib.auth.forms import UserCreationForm  # 导入Django自带的注册表单
from django.utils import timezone
from django.shortcuts import get_object_or_404


def course_list(request):
    # 从数据库获取所有课程
    all_courses = Course.objects.all()
    # 把课程数据传给网页模板
    return render(request, 'courses/course_list.html', {'courses': all_courses})


def user_login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        # 校验账号密码
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('course_list')  # 登录成功跳到首页
        else:
            return render(request, 'courses/login.html', {'error': '用户名或密码错误'})
    return render(request, 'courses/login.html')


def user_logout(request):
    logout(request)
    return redirect('course_list')


@login_required
def enroll_course(request, course_id):
    course = Course.objects.get(id=course_id)
    # 创建选课记录 (如果已存在则不创建)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('my_courses')


@login_required
def my_courses(request):
    # 查询当前用户的所有选课记录，并关联查询课程信息
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/my_courses.html', {'enrollments': enrollments})


def user_register(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        # 简单的校验：用户名是否已存在
        if User.objects.filter(username=u).exists():
            return render(request, 'courses/register.html', {'error': '用户名已存在'})
        # 创建用户
        user = User.objects.create_user(username=u, password=p)
        return redirect('login')  # 注册成功去登录
    return render(request, 'courses/register.html')


@login_required
def drop_course(request, course_id):
    # 找到该学生对应的这门课记录并删除
    Enrollment.objects.filter(student=request.user, course_id=course_id).delete()
    return redirect('my_courses')


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    comments = course.comments.all().order_by('-created_at')  # 获取该课所有评论

    if request.method == 'POST' and request.user.is_authenticated:
        text = request.POST.get('comment_text')
        if text:
            Comment.objects.create(course=course, user=request.user, text=text)
            return redirect('course_detail', course_id=course.id)

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'comments': comments
    })


# 1. 查看已选课程的作业列表
@login_required
def assignment_list(request):
    # 找到学生选的所有课
    my_enrollments = Enrollment.objects.filter(student=request.user)
    my_courses = [en.course for en in my_enrollments]
    # 找到这些课对应的所有作业
    assignments = Assignment.objects.filter(course__in=my_courses)
    return render(request, 'courses/assignment_list.html', {'assignments': assignments})


# 2. 提交作业页面
@login_required
def submit_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    # 检查是否已经提交过
    submission = StudentSubmission.objects.filter(assignment=assignment, student=request.user).first()

    if request.method == 'POST':
        answer_text = request.POST.get('answer')
        if submission:
            submission.answer = answer_text  # 修改已有的
            submission.save()
        else:
            StudentSubmission.objects.create(
                assignment=assignment,
                student=request.user,
                answer=answer_text
            )
        return redirect('my_scores')  # 提交后去分数页查看状态

    return render(request, 'courses/submit_assignment.html', {
        'assignment': assignment,
        'submission': submission
    })


# 3. 分数查询页面
@login_required
def my_scores(request):
    # 找到该学生所有的作业提交记录（包含分数）
    submissions = StudentSubmission.objects.filter(student=request.user)
    return render(request, 'courses/my_scores.html', {'submissions': submissions})

def home(request):
    # 首页不需要查询所有课程，保持逻辑独立
    return render(request, 'courses/home.html')

@login_required
def delete_comment(request, comment_id):
    # 查找评论，确保是本人且存在
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    course_id = comment.course.id
    comment.delete()
    # 删完直接跳回去
    return redirect('course_detail', course_id=course_id)

def course_chat(request):
    courses = Course.objects.all()  # 获取所有课程作为频道
    return render(request, 'courses/chat_hub.html', {'courses': courses})