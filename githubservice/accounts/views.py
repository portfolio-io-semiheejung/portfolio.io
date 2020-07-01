from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('mains:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('mains:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)    


def login(request):
    if request.user.is_authenticated:
        return redirect('mains:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user) 
            return redirect('mains:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request,'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


@login_required
def profile(request, username):
    user_profile = get_object_or_404(get_user_model(),username=username) 
    context ={
        'user_profile': user_profile,
    }
    print('--------------------------------------------------------------------------------',user_profile )
    return render(request,'accounts/profile.html', context)
