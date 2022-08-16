from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('instance_create/', views.openstack_create.as_view()), #url 합치기
    path('instance_info/', views.openstack_list.as_view()),
]