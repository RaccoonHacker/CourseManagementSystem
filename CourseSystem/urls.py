from django.contrib import admin
from django.urls import path, include # 记得导入 include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')), # 把首页交给 courses 模块处理
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)