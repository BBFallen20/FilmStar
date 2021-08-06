from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.apps.films.models import Film
from api.apps.films.serializers.film_serializers import FilmSerializer


class FilmListAPI(generics.ListAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self):
        return Film.objects.all()


class FilmDetailAPI(generics.RetrieveAPIView):
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def get_queryset(self):
        try:
            return Film.objects.filter(slug=self.kwargs.get('slug'))
        except Film.DoesNotExist:
            raise Http404
