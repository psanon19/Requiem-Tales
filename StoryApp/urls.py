from django.urls import path
from django.contrib import admin


from . import views

urlpatterns = [
    path('', views.userindex, name='userindex'),
    path('admin/', admin.site.urls),
    path('createUser/', views.createUser, name='createUser'),
    path('post/<int:pk>/', views.post_detail, name='detail'),
    path('user/',views.index, name='index'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/test/', views.test_post, name='test')
    ]
