from django.urls import path
from . import views

urlpatterns = [
    # token
    #path('login/', views.login_view, name='login'),
    #path('', views.profile_view, name='profile'),
    #path('profile/', views.profile_view, name='profile'),
    # jwt
    path('login/', views.login_view_jwt, name='login'),
    path('', views.profile_view_jwt, name='profile'),
    path('profile/', views.profile_view_jwt, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]