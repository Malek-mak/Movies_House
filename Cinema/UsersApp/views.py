from django.shortcuts import render, redirect
from django.http import request
from django.contrib.auth import authenticate, login, logout
from Movies_House.models import MyUser, Movies_List_db, Ticket
from .forms import SignUpForm, LogInForm
from django.contrib import messages 


def SignUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signed Up Succufully")
            return redirect('login')
    else:
          form = SignUpForm()  
          
    return render(request, 'UsersT/signUp.html', {'form': form})


def LogIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else :
            messages.error(request, 'User not found') 
            return redirect('login')   
    else :
          form = LogInForm()
    return render(request, 'UsersT/logIn.html', {'form': form})

def LogOut(request):
    logout(request)
    return redirect('home')

def MyMovies(request):
    u = request.user
    data = Ticket.objects.filter(user=u)
    return render(request, 'UsersT/mymovies.html', {'data': data})