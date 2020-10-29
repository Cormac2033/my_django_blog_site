from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views




urlpatterns = [
    # 127.0.0.1.8000 --> local
    # gra-productions.com --> online for example
    path('', views.post_list, name='post_list'),

    # 127.0.0.1.8000/post/2 --> local
    # gra-productions.com/post/2 --> online
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # 127.0.0.1.8000/post/new --> local
    # gra-productions.com/post/new --> online
    path('post/new/', views.post_new, name='post_new'),

    # 127.0.0.1.8000/post/2/edit --> local
    # gra-productions.com/post/2/edit --> online
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    # 127.0.0.1.8000/drafts --> local
    # gra-productions.com/drafts --> online
    path('drafts/', views.post_draft_list, name='post_draft_list'),

    # 127.0.0.1.8000/2/publish --> local
    # gra-productions.com/2/publish --> online
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),

    # Below from CP PYP Mod 13 pt 11 this has been updated...
    # path('accounts/login/', auth_views.login, name='login'),
    # Alternative in Django docs...
    # path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),

    # 127.0.0.1.8000/accounts/login --> local
    # gra-productions.com/accounts/login --> online
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]
