from django.urls import path 
from . import views

app_name = 'post' 


urlpatterns = [
    path('groups/<slug:pk>/', views.group_posts, name='group_page'),
    path('', views.index, name='main_page')
]