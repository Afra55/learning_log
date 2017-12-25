from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'topics/', views.topics, name='topics'),
    path(r'topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
    path(r'new_topic/', views.new_topic, name='new_topic'),
    path(r'new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),
    path(r'edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name='edit_entry')
]
