from django import forms
from Movies_House.models import MyUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ( 'first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name' ,'class': 'rounded-xl text-black px-3 py-3 m-3 border'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name' ,'class': 'rounded-xl text-black px-3 py-3 m-3 border'}))
        
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username' ,'class': 'rounded-xl text-black px-3 py-3 m-3 border'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email' ,'class': 'rounded-xl text-black px-3 py-3 m-3 border'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password' ,'class': 'rounded-xl text-black px-3 py-3 m-3 border'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat' ,'class': 'rounded-xl text-black px-3 py-3 m-3 border'}))

class LogInForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username' ,'class': 'rounded-xl text-black px-3 py-3 m-3 border'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password' ,'class': 'rounded-xl text-black px-3 py-3 m-3 border'}))
