from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path(r'', include('app_blog.urls')),
]
# Register your models here.
