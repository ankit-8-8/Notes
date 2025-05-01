from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('edit/', views.edit, name='edit'),
    path('details/', views.detail, name='details'),
    path('search/', views.search, name='search'),
    path('sort/', views.sort, name='sort'),
    path('delete/', views.delete, name='delete'),
    path('likes/', views.likes, name='likes'),
    # path('comment/', views.add_comment, name='add_comment'),
]