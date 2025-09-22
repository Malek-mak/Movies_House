from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name='home'),
    path("Movies/", views.Movies, name='movies'),
    path("About_Us/", views.About, name='about'),
    path('Movie/<int:id>/', views.Movie_Details, name='movie_detail'),
    path('Edit/<int:id>/', views.Edit, name='edit'),
    path('Delete/<int:id>/', views.Delete, name='delete'),
    path("available-seats/<int:movie_id>/<int:date_id>/", views.available_seats, name="available_seats"),

]
