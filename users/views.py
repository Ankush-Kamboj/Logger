from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import resolve_url
from .models import Profile


# HomePage
def homepage(request):
    current_user = request.user
    details = Profile.objects.filter(user=current_user).first()
    
    if details:
        return render(request, 'users/homepage.html', {'users':details})
    else:
        return render(request, 'users/homepage.html')


# Register Page
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            return redirect('users-login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form':form})


# Create Profile Page - Login is required for this Page
@login_required
def createProfile(request):
    current_user = request.user
    details = Profile.objects.filter(user=current_user).first()
    
    if details:
        return render(request, 'users/homepage.html', {'users':details})
    
    else:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                details = form.save(commit=False)
                details.user = request.user
                details.save()
                return redirect('users-homepage')
        else:
                form = ProfileForm()
    
    return render(request, 'users/createProfile.html', {'form':form})


# Login Page
class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return resolve_url('users-create-profile')


# Logout Page
class LogoutView(auth_views.LogoutView):
    template_name = 'users/logout.html'