# Importing required libraries
from django.urls import path
from . import views

# Url patterns for Books app module of Library Management System
urlpatterns = [
    # Home page URL
    path('', views.home, name='home'),

    # Issue page URL
    path('issue', views.issue, name='issue'),

    # Login page URL
    path('login/', views.login, name='login'),

    # Register page URL
    path('register/', views.register, name='register'),

    # Logout page URL
    path('logout', views.logout, name='logout'),

    # Return item page URL
    path('return_item', views.return_item, name='return_item'),

    # History page URL
    path('history', views.history, name='history'),
]
