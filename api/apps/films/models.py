import datetime

from django.db import models
from django.db.models.sql import Query
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField


def film_title_image_upload_path(instance, filename) -> str:
    return f"films/{instance.title}/{filename}"


def film_additional_image_upload_path(instance, filename) -> str:
    return f"films/{instance.film.title}/{filename}"


def film_actor_image_upload_path(instance, filename) -> str:
    return f"actors/{instance.first_name}_{instance.last_name}/{filename}"


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


class FilmActor(models.Model):
    image = models.ImageField(upload_to='', verbose_name=_('Actor`s image'))
    first_name = models.CharField(max_length=100, verbose_name=_('Actor`s first name'))
    last_name = models.CharField(max_length=100, verbose_name=_('Actor`s last name'))
    birth_date = models.DateField(verbose_name=_('Actor`s birth date'))

    @property
    def film_list(self) -> Query:
        return self.film_actors.all()

    def __str__(self) -> str:
        return f"Actor {self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        return f"Actor({self.first_name} {self.last_name})"

    class Meta:
        verbose_name = _('Film actor')
        verbose_name_plural = _('Films actors')


class FilmManufacturer(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('Film manufacturer title'))
    country = models.CharField(max_length=150, verbose_name=_("Manufacturer country"))

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"FilmManufacturer({self.title})"


class Film(models.Model):
    title_image = models.ImageField(upload_to=film_title_image_upload_path, verbose_name=_("Film image"))
    title = models.CharField(max_length=150, verbose_name=_('Film title'))
    description = models.TextField(max_length=150, verbose_name=_('Film description'))
    genres = models.ManyToManyField(FilmGenre, related_name='film_genres', verbose_name=_('Film genres'))
    actors = models.ManyToManyField(FilmActor, related_name='film_actors', verbose_name=_('Film actors'))
    duration = models.DurationField(verbose_name=_('Film duration'), default=datetime.timedelta(hours=1))
    manufacturer = models.OneToOneField(FilmManufacturer, on_delete=models.CASCADE, verbose_name=_('Film manufacturer'))
    slug = AutoSlugField(unique=True, populate_from='title', verbose_name=_('Film slug'))

    @property
    def genre_list(self) -> Query:
        return self.genres.all()

    @property
    def actor_list(self) -> Query:
        return self.actors.all()

    @property
    def image_list(self) -> Query:
        return self.film_film_image.all()

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"Film({self.title})"

    class Meta:
        verbose_name = _('Film')
        verbose_name_plural = _('Films')


class FilmImage(models.Model):
    image = models.ImageField(upload_to=film_additional_image_upload_path, verbose_name=_("Film image"))
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('Image description'))
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name='film_film_image',
        verbose_name=_('Image film')
    )

    def __str__(self) -> str:
        return f"{self.film.title} image #{self.pk}"

    def __repr__(self) -> str:
        return f"FilmImage({self.film.title} image #{self.pk})"

    class Meta:
        verbose_name = _('Film image')
        verbose_name_plural = _('Films images')
