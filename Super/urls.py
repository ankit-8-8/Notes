from django.urls import path
from .import views

urlpatterns = [
    path('admin-home/', views.admin_home, name='admin-home'),
    path('admin-login/', views.admin_login, name='admin-login'),
    path('admin-logout/', views.admin_logout, name='admin-logout'),
    path('admin-register/', views.admin_register, name='admin-register'),
    path('add-user/', views.add_user, name='add-user'),
    path('delete-user/', views.delete_user, name='delete-user'),
]