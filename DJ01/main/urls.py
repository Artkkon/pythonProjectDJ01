from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('data/', views.data),
    path('test/', views.test),
]