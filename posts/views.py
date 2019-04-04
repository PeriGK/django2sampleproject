from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Posts
from .forms import PostsForm
from .serializers import UserSerializer, GroupSerializer, PostSerializer


def index(request):
    data = Posts.objects.all()
    context = {'data': data}
    return render(request, 'posts/index.html', context)


def detail(request, postid):
    post = get_object_or_404(Posts, pk=postid)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)


@login_required
def post_form(request):
    if request.method == 'GET':
        form = PostsForm()
    else:
        form = PostsForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            post = Posts.objects.create(title=title, body=body, userId=request.user)
            return HttpResponseRedirect("/posts/"+str(post.id))
    return render(request, 'posts/newpost.html', {'form': form, 'url_redirect': 'posts'})


@login_required
def delete_post(request, postid=None):

    if request.method == "GET":
        post = get_object_or_404(Posts, id=postid)

        post.delete()
        messages.success(request, "Post successfully deleted!")
        return HttpResponseRedirect('/posts/')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset=Posts.objects.all()
    serializer_class = PostSerializer
