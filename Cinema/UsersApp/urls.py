from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LogIn, name='login'),
    path('signup/', views.SignUp, name='signup'),
    path('Logout/', views.LogOut, name='logout'),
    path('My_Movies/', views.MyMovies, name='mymovies'),
    
]
