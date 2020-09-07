from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ('name', 'college_name', 'degree', 'passout_year', 'course_name', 'age',)  