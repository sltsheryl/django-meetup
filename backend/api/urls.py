from django.urls import path
from . import views

# endpoints
urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('meetups/', views.getMeetups, name="meetups"),
     path('meetups/<str:pk>/', views.getMeetup, name="meetup"),
        path('favorites/', views.getFavs, name="favorites"),
    path('new-meetup/', views.createMeetup, name="create-meetup"),
     path('meetups/<str:pk>/modify-fav/', views.modifyFav, name="modify-fav"),

]
