from rest_framework import serializers

from api.apps.films.models import FilmGenre, FilmManufacturer, FilmActor, Film, FilmImage


class FilmImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmImage
        exclude = ('id', 'film')


class FilmGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmGenre
        exclude = ('id',)


class FilmManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmManufacturer
        exclude = ('id',)


class FilmActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmActor
        exclude = ('id',)


class FilmSerializer(serializers.ModelSerializer):
    genres = FilmGenreSerializer(source='genre_list', many=True)
    actors = FilmActorSerializer(source='actor_list', many=True)
    images = FilmImageSerializer(source='image_list', many=True)
    manufacturer = FilmManufacturerSerializer()

    class Meta:
        model = Film
        fields = ('title', 'title_image', 'description', 'genres', 'actors', 'duration', 'manufacturer', 'images')
