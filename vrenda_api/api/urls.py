from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'flows', views.FlowsViewSet, basename='flow')
# router.register(r'health-check', views.health_check)

# urlpatterns = [
#     path('health-check/', views.health_check)
# ]

urlpatterns = router.urls

urlpatterns.append(path('health-check/', views.health_check))
