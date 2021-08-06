from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/film_api/', include('api.apps.films.urls')),
    path('api/profiles/', include('api.apps.profiles.urls'))
]
