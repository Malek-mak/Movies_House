from django import forms
from .models import Movies_List_db, MyUser, SEAT_CHOICES, Ticket, row_choices, col_choices, SeatModel, PlayDates



    
class TicketForm(forms.ModelForm):
    class Meta:
        model= Ticket
        fields= ('date', 'seat')
    
    def __init__(self, *args, **kwargs):
        movie = kwargs.pop('movie', None) 
        super().__init__(*args, **kwargs)

        # populate only playdates for this movie
        if movie:
            self.fields['date'].queryset = PlayDates.objects.filter(movie=movie)

        #populate seats
        if 'date' in self.data:
            try:
                date_id = int(self.data.get('date'))
                booked_seats = Ticket.objects.filter(date_id=date_id).values_list('seat_id', flat=True)
                self.fields['seat'].queryset = SeatModel.objects.exclude(id__in=booked_seats)
            except (ValueError, TypeError):
                pass
        else:
            # if no date selected yet, don't show any seats
            self.fields['seat'].queryset = SeatModel.objects.none()
  