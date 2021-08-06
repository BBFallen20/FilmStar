from rest_framework import generics

from api.apps.films.models import Film
from api.apps.films.serializers.film_serializers import FilmSerializer


class FilmListAPI(generics.ListAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self):
        return Film.objects.all()
