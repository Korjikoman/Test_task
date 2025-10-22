from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('api/places.geojson/', views.places_geojson, name='places-geojson'),
    path('api/places/<int:place_id>/', views.place_detail, name='place-detail'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)