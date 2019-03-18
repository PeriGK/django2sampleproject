from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts



def index(request):
    data = Posts.objects.all()
    context = {'data' : data}
    return render(request, 'posts/index.html', context)
