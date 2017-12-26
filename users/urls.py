from django.contrib.auth.views import login  # 使用默认视图 login
from django.urls import path

from users import views

urlpatterns = [
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),  # http://localhost:8000/users/login/
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register')
]
