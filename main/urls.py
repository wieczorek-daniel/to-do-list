from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_task/', views.createTask, name='create_task'),
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),
]
