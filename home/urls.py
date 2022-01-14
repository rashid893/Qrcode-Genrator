from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views

urlpatterns = [
path('',views.index,name="index"),
path('send/',views.send,name="send"),
]