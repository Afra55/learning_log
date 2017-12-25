from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse

from learning_logs.forms import TopicForm
from learning_logs.models import Topic


def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    if request.method != 'POST':  # 判断请求的方法
        form = TopicForm()
    else:
        form = TopicForm(request.POST)

    if form.is_valid():  # 验证表单字段是否都填写了（默认都必须填写）
        form.save()  # 将表单数据写入数据库
        return HttpResponseRedirect(reverse('learning_logs:topics'))  # 重定向 URL

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
