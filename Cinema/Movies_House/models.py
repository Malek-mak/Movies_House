from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe
import string

from django.utils.timezone import datetime, now


class MyUser(AbstractUser): 

    username = models.CharField(max_length=150, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    joined_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username



class Genre_db(models.Model):
    OPTIONS = [
        ("Action", "Action"),
        ("Crime", "Crime"),
        ("Comedy", "Comedy"),
        ("Drama", "Drama"),
        ("Adventure", "Adventure"),
        ("Romance", "Romance"),
        ("Sci-Fi", "Sci-Fi"),
        ]
    genre_name = models.CharField(max_length=30, choices=OPTIONS)
    def __str__(self):
        return self.genre_name





            
RED_SEAT_SVG = """<?xml version="1.0" encoding="UTF-8"?>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64" role="img" aria-label="Seat">
    <!-- backrest (explicit red) -->
    <rect x="14" y="6" width="36" height="18" rx="4" fill="#b71c1c" />
    <rect x="14" y="6" width="36" height="18" rx="4" fill="none" stroke="rgba(0,0,0,0.12)" />
    <!-- cushion / seat (explicit red) -->
    <rect x="8" y="26" width="48" height="22" rx="5" fill="#d32f2f" />
    <rect x="8" y="26" width="48" height="22" rx="5" fill="none" stroke="rgba(0,0,0,0.12)" />
    <!-- highlight -->
    <path d="M12 30c0-2 3-4 8-4h24c5 0 8 2 8 4v6c0 2-3 4-8 4H20c-5 0-8-2-8-4v-6z"
            fill="rgba(255,255,255,0.18)" />
    </svg>"""

# first 10 letters A-J
LETTERS = list(string.ascii_uppercase[:10])  # ['A', 'B', ..., 'J']

# numbers 1..10
NUMBERS = range(1, 11)

# Choices: value is e.g. "1A", "10J"; label is the red SVG (marked safe so it renders as HTML)
SEAT_CHOICES = [
        (f"{num}{letter}", f"{num}{letter}")  for num in NUMBERS for letter in LETTERS
    ]         
col_choices = [
    (f"{c}", f"{c}") for c in LETTERS 
]   
row_choices = [
    (f"{str(n)}", f"{str(n)}") for n in NUMBERS 
]  


            
class Movies_List_db(models.Model):
    name = models.CharField(max_length=80)
    discription = models.TextField()
    year = models.IntegerField(default=2000)
    duration = models.IntegerField()
    genre = models.ManyToManyField(Genre_db)
    image = models.ImageField(upload_to='movie_poster/',null=False, blank=False)
    price = models.FloatField()
    booked_out = models.CharField(max_length=15, choices=[('yes', 'Booked Out'), ('no', 'Available')], default='no')
    rating = models.FloatField()
    
    added_at = models.DateTimeField(auto_now_add=True)
    def save(self):
        if self.tickets_left == 0:
            self.booked_out = 'yes'
        super().save()
        
    def __str__(self):
        return self.name
    
class PlayDates(models.Model):
    movie = models.ForeignKey(Movies_List_db, related_name='showtimes', on_delete=models.CASCADE, default='None')
    tickets_left = models.IntegerField(default=100)
    date = models.DateTimeField()
    def __str__(self):
        return f'{self.date}'
    
    class Meta:
        unique_together = ('movie', 'date')
    
    
    
class SeatModel(models.Model):
    
    col = models.CharField(max_length=2, choices=col_choices)
    row = models.CharField(max_length=2, choices=row_choices)
    def __str__(self):
        return f"{self.col}{self.row}"
    class Meta:
        unique_together = ('col', 'row')
        
    

    
    
class Ticket(models.Model):
    user = models.ForeignKey(MyUser, related_name='tickets_booked', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies_List_db, on_delete=models.CASCADE)
    date = models.ForeignKey(PlayDates,related_name='tickets', on_delete=models.CASCADE)
    seat = models.ForeignKey(SeatModel, on_delete=models.CASCADE, default='A2')
    booked_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('date', 'seat')
        
    def __str__(self):
        return f"{self.user} booked seat {self.seat} of {self.movie} at {self.date}"
     
        
        
    
    
    
    


    

    
    
    
    
    

    
    
