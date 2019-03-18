from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Posts


@login_required
def index(request):
    data = Posts.objects.all()
    context = {'data' : data}
    return render(request, 'posts/index.html', context)

def detail(request, postid):
    post = Posts.objects.get(pk=postid)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)