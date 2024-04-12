from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('health-check/', views.health_check)
]
