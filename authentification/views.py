from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
from django.conf import settings
from authentification import forms
from authentification.models import UserProfile
def logout_user(request):
    logout(request)
    return redirect('login')

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect('dashboard')
            else:
                message = 'invalid user.'
    return render(
        request, 'authentification/login.html', context={'form': form, 'message': message})

def signup_page(request):
    form = forms.SignupForm()
    message =''
    if request.method =='POST':
        form =forms.SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            UserProfile.objects.create(username =user, first_name=user.first_name,last_name=user.last_name, email=user.email,domaine=form.cleaned_data['domaine'],phone=form.cleaned_data['phone']).save
            login(request, user)
            return redirect('dashboard')
        else:
            message = 'invalid field.'
        
    
    return render(request,'authentification/signup.html',context={'form':form,'message':message})