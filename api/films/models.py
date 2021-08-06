from django.db import models
from django.db.models.sql import Query
from django.utils.translation import ugettext_lazy as _


def film_title_image_upload_path(instance, filename):
    return f"films/{instance.title}/{filename}"


class FilmGenre(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('Genre title'))
    description = models.TextField(max_length=1500, verbose_name=_('Genre description'))

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"FilmGenre({self.title})"

    @property
    def films(self) -> Query:
        return self.film_genres.all()

    class Meta:
        verbose_name = _('Film Genre')
        verbose_name_plural = _('Films Genres')


class Film(models.Model):
    title_image = models.ImageField(upload_to=film_title_image_upload_path)
    title = models.CharField(max_length=150, verbose_name=_('Film title'))
    description = models.TextField(max_length=150, verbose_name=_('Film title'))
    genres = models.ManyToManyField(FilmGenre, related_name='film_genres', verbose_name=_('Film genres'))

    @property
    def genre_list(self) -> Query:
        return self.genres.all()

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"Film({self.title})"

    class Meta:
        verbose_name = _('Film')
        verbose_name_plural = _('Films')
