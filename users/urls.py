from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as users_views


urlpatterns = [
    path('', users_views.homepage, name='users-homepage'),
    path('register/', users_views.register, name='users-register'),
    path('login/', users_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    path('createprofile/', users_views.createProfile, name='users-create-profile'),
    ]