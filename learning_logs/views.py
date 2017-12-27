from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.urls import reverse

from learning_logs.forms import TopicForm, EntryForm
from learning_logs.models import Topic, Entry


def index(request):
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    if request.method != 'POST':  # 判断请求的方法
        form = TopicForm()
    else:
        form = TopicForm(request.POST)

    if form.is_valid():  # 验证表单字段是否都填写了（默认都必须填写）
        new_topic = form.save(commit=False)
        new_topic.owner = request.user
        new_topic.save()  # 将表单数据写入数据库
        return HttpResponseRedirect(reverse('learning_logs:topics'))  # 重定向 URL

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

    if form.is_valid():
        new_entry = form.save(commit=False)
        new_entry.topic = topic
        new_entry.save()
        return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
