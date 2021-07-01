from django.contrib import admin
from django.urls import path
from django.conf import Settings
from .views import index,blog

urlpatterns=[
    path('blog/',blog,name='bloh')
]