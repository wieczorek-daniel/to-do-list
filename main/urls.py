from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings, name="settings"),
    path('change_password/', views.changePassword, name="change_password"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="main/password_reset.html", email_template_name='main/password_reset_email.html'), name="password_reset"),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name="main/password_reset_done.html"), name="password_reset_done"),
    path('reset_password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password/complete/', auth_views.PasswordResetCompleteView.as_view(template_name="main/password_reset_complete.html"), name="password_reset_complete"),
    path('create_task/', views.createTask, name='create_task'),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),
    path('calendar/', views.calendar, name='calendar'),
]
