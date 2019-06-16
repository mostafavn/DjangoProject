from django.contrib import admin
from django.urls import path
from . import views


app_name = 'en'

urlpatterns = [
    path('', views.en, name='en'),
]
