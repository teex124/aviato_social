from django.urls import path 
from . import views

urlpatterns = [
    path('groups/<slug:pk>/', views.group_posts),
    path('', views.index)
]