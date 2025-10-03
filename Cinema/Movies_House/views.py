from django.shortcuts import render, redirect
from django.http import request, JsonResponse
from .models import MyUser, Movies_List_db, Ticket, PlayDates, SeatModel, Genre_db
from .forms import TicketForm
from django.contrib import messages
from django.db.models import Q


def Home(request):
    latest_movies = Movies_List_db.objects.all().order_by('-added_at')[0: 4]
    famous_movies = Movies_List_db.objects.all().order_by('-rating')[0: 4]
    return render(request, 'Movies/home.html', {'latest_movies': latest_movies,
                                                'famous_movies': famous_movies})

def Movies(request):
    genres = Genre_db.objects.all()
    movies = Movies_List_db.objects.all()
    search = request.GET.get('search', '')
    genre = request.GET.get('genre', '')
    
    if genre :
        movies = movies.filter(genre=request.GET.get('genre'))
    elif search:
        movies = movies.filter(Q(name__icontains=search) | Q(discription__icontains=search))
    else:
        movies = Movies_List_db.objects.all()
        
    return render (request, 'Movies/movies.html', {'movies': movies, 'genres': genres})


def About(request):
    return render (request, 'Movies/about.html')

def Movie_Details(request, id):
    movie = Movies_List_db.objects.get(id=id)
    dates = PlayDates.objects.filter(movie=movie)
    
    if request.method == 'POST':
        form = TicketForm(request.POST or None, movie=movie)
        
        if form.is_valid():
            frm = form.save(commit=False)
            frm.user = request.user
            frm.movie = movie
            date = form.cleaned_data['date']
            frm.save()
            movie_seats = PlayDates.objects.get(movie=movie, date=str(date))
            movie_seats.tickets_left = movie_seats.tickets_left - 1
            movie_seats.save()
            messages.success(request, f"Ticket booked succesfully")
            return redirect('movie_detail', id=id)
        else:
            messages.error(request, f"{form}")
            return redirect('movie_detail', id=id)
        
    else:
        form = TicketForm(movie=movie)

    return render(request, 'Movies/movie_details.html', {'movie': movie,
                                                         'form': form})

def available_seats(request, movie_id, date_id):
    
    # Find already booked seats for this date
    booked_seats = Ticket.objects.filter(date_id=date_id).values_list('seat_id', flat=True)

    # All seats except booked ones
    seats = SeatModel.objects.exclude(id__in=booked_seats)


    data = [
        {"id": seat.id, "label": f"{seat.row}{seat.col}"}
        for seat in seats
    ]
    return JsonResponse(data, safe=False)

def Edit(request, id):
    ticket = Ticket.objects.get(id=id)
    movie = ticket.movie
    inital_date = ticket.date
    initial_seat = ticket.seat
    if request.method == 'POST':
        form = TicketForm(request.POST, movie=movie)
        if form.is_valid():
            ticket.date = form.cleaned_data['date']
            ticket.seat = form.cleaned_data['seat']
            ticket.save()
            messages.success(request, f"Ticket Edited from {inital_date} Seat {initial_seat}  to  {form.cleaned_data['date']} Seat {form.cleaned_data['seat']} succufully")
            return redirect('mymovies')
    else :
        form = TicketForm(movie=movie)
        
    return render (request, 'Movies/edit.html', {'form': form, 
                                                 'ticket': ticket})

def Delete(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.delete()
    messages.success(request, 'Ticket Deleted Succufully')
    return redirect('mymovies')
        
        