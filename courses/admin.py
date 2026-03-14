from django.contrib import admin
from .models import Course, Enrollment, Assignment, StudentSubmission  # 引入你写的课程模型


# 修饰后台展示的样子
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # 在列表页显示的字段
    list_display = ('title', 'teacher', 'image')
    # 添加搜索框，可以按课程名和老师名搜索
    search_fields = ('title', 'teacher')
    # 右侧添加过滤器
    list_filter = ('teacher',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date_enrolled')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'create_time')
    list_filter = ('course',)

# 管理员在这里看学生的答案并录入分数
@admin.register(StudentSubmission)
class StudentSubmissionAdmin(admin.ModelAdmin):
    list_display = ('student', 'assignment', 'score', 'graded_time')
    # 设置哪些字段可以点击进入修改页面进行打分
    list_editable = ('score',)
    list_filter = ('assignment__course', 'student')
from django.contrib import admin

# Register your models here.
