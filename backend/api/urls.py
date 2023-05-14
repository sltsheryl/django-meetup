from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


# endpoints
urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('meetups/', views.getMeetups, name="meetups"),
     path('meetups/<str:pk>/', views.getMeetup, name="meetup"),
        path('favorites/', views.getFavs, name="favorites"),
    path('new-meetup/', views.createMeetup, name="create-meetup"),
     path('meetups/<str:pk>/modify-fav/', views.modifyFav, name="modify-fav"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
