from django.conf.urls.static import static
from django.urls import path

from api.settings import settings
from .views.film_views import FilmListAPI


urlpatterns = [
    path('films/', FilmListAPI.as_view(), name='films-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
