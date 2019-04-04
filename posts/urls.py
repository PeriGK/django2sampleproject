from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:postid>/', views.detail, name='detail'),
    path('delete/<int:postid>/', views.delete_post, name='delete'),
    path('new/', views.post_form,name='create'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]
