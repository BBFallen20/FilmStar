from django.conf.urls.static import static
from django.urls import path

from api.settings import settings
from .views.film_views import FilmListAPI, FilmDetailAPI

urlpatterns = [
    path('films/', FilmListAPI.as_view(), name='films-list'),
    path('film/<slug:slug>/', FilmDetailAPI.as_view(), name='film-by-id'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
