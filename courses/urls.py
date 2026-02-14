# courses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 1. 核心导航页面
    path('', views.home, name='home'),  # 唯一的空路径，指向你的黑科技首页
    path('courses/', views.course_list, name='course_list'),  # 课程列表页
    path('my-courses/', views.my_courses, name='my_courses'),  # 我的课表

    # 2. 身份验证
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # 3. 课程操作逻辑
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),  # 详情/交流页
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
    path('drop/<int:course_id>/', views.drop_course, name='drop_course'),

    # 4. 作业与分数
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('submit-assignment/<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),
    path('my-scores/', views.my_scores, name='my_scores'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('chat/', views.course_chat, name='course_chat'),
]