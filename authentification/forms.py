from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="", widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Username'}))
    password = forms.CharField(max_length=63, label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))


class SignupForm(UserCreationForm):
    username = forms.CharField(label="", max_length=30,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Username'}))
    last_name = forms.CharField(label="", max_length=30,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Last name'}))
    first_name = forms.CharField(label="", max_length=30,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'First name'}))
    email= forms.EmailField(label="", max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Email'}))
    phone= forms.CharField(label="", max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Phone'}))
    domaine = forms.CharField(label="", max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Domaine'}))
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username','email','first_name',
                  'last_name','phone','domaine']
        