from django.contrib import admin
from .models import Film, FilmGenre, FilmActor, FilmManufacturer, FilmImage


class FilmImageInline(admin.TabularInline):
    model = FilmImage
    extra = 1


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    inlines = [FilmImageInline]


@admin.register(FilmGenre)
class FilmGenreAdmin(admin.ModelAdmin):
    pass


@admin.register(FilmActor)
class FilmActorAdmin(admin.ModelAdmin):
    pass


@admin.register(FilmManufacturer)
class FilmManufacturerAdmin(admin.ModelAdmin):
    pass
