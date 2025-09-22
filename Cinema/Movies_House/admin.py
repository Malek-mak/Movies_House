from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin


admin.site.register(models.MyUser, UserAdmin)
admin.site.register(models.PlayDates)
admin.site.register(models.SeatModel)
admin.site.register(models.Genre_db)
admin.site.register(models.Ticket)


@admin.register(models.Movies_List_db)
class MoviesAdmin(admin.ModelAdmin):
    filter_horizontal = ("genre",)
