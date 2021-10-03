from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings, name="settings"),
    path('change_password/', views.changePassword, name="change_password"),
    path('create_task/', views.createTask, name='create_task'),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),
    path('calendar/', views.calendar, name='calendar'),
]
