from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:postid>/', views.detail, name='detail'),
    path('new/', views.post_form,name='create')
]

