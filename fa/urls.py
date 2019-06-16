from django.contrib import admin
from django.urls import path
from . import views


app_name = 'fa'

urlpatterns = [
    path('', views.fa, name='fa'),
]
