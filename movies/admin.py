from django.contrib import admin
from .models import Genre, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    exclude = ("date_created",)
    list_display = ("name", "number_in_stock", "daily_rate")
