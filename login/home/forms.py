from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from home.models import Profile
from django import forms

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')

# class SignUpForm(UserCreationForm):
#     username = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
#     first_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name')
#     last_name=forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name')
#     email=forms.EmailField(forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Enter a valid email address')
#     password1=forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
#     password2=forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#         # I've tried both of these 'fields' declaration, result is the same
#         # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
#         fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('bio','location','birth_date')
