from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'topics/', views.topics, name='topics'),
    path(r'topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
    path(r'new_topic/', views.new_topic, name='new_topic')
]
