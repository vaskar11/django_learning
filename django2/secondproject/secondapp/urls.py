from django.contrib import admin
from django.urls import path
from secondapp import views

urlpatterns = [
    path('second/', views.secondindex)
]