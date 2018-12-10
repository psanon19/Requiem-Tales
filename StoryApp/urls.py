from django.urls import path
from django.contrib import admin


from . import views

urlpatterns = [
    path('', views.userindex, name='userindex'),
    path('admin/', admin.site.urls),
    path('createUser/', views.createUser, name='createUser'),
    path('user/',views.index, name='index'),
    ]
