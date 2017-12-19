from django.urls import path

from . import views


urlpatterns = [
    path(r'', views.index, name='index'),     # '^$' 查找开头到末尾的 URL 与基础 URL(http://127.0.0.1:8000/) 匹配
]
