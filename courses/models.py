from django.db import models
from django.contrib.auth.models import User  # 导入系统自带的用户模型


class Course(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # 新增图片字段，upload_to 指定上传到 media/course_images/ 目录下
    # default 建议设置一个默认图，防止管理员没上传时报错
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)

    def __clstr__(self):
        return self.title


class Enrollment(models.Model):
    # 关联学生 (当学生账号被删除时，选课记录也随之删除)
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="学生")
    # 关联课程
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    # 选课时间
    date_enrolled = models.DateTimeField(auto_now_add=True, verbose_name="选课时间")

    class Meta:
        # 防止同一个学生重复选同一门课
        unique_together = ('student', 'course')
        verbose_name = "选课记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.student.username} 选了 {self.course.title}"

# 1. 课程作业模型 (管理员发布)
class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="所属课程")
    title = models.CharField(max_length=200, verbose_name="作业标题")
    content = models.TextField(verbose_name="作业要求/知识点")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")

    class Meta:
        verbose_name = "课程作业"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"【{self.course.title}】{self.title}"

# 2. 学生提交与成绩模型 (学生作答，管理员打分)
class StudentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, verbose_name="对应作业")
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="学生")
    answer = models.TextField(verbose_name="学生作答内容")
    score = models.IntegerField(null=True, blank=True, verbose_name="评分 (0-100)")
    graded_time = models.DateTimeField(null=True, blank=True, verbose_name="打分时间")

    class Meta:
        unique_together = ('assignment', 'student') # 一个学生对一个作业只能交一次
        verbose_name = "学生作业提交"
        verbose_name_plural = verbose_name

class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="内容")
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models

# Create your models here.
