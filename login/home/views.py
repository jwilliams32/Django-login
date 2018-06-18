from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import Profile
from .forms import UserForm, ProfileForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# @login_required
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            return redirect('profile.html')
    else:
        form = AuthenticationForm()
    #
    # template = 'login.html'
    # context = {}
    # # return HttpResponse("Login")

    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # email = form.cleaned_data['email']
            # first_name = form.cleaned_data['']
            # last_name = form.cleaned_data['']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


