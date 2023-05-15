from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import path
from .models import Meetup
from . import views
from .serializers import MeetupSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
    {
        "endpoint": "/",
        "method": "GET",
        "body": None,
        "description": "Returns all the meetups"
    },
    {
        "endpoint": "/new-meetup",
        "method": "POST",
        "body": {"title": "", "description": "", "location": "", "image": ""},
        "description": "Create a new meetup"
    }, 
    {
        "endpoint": "/favorites",
        "method": "GET",
        "body": None,
        "description": "Returns all the favorites"
    }
]
    return Response(routes)

@api_view(['GET'])
def getMeetups(request):
    meetups = Meetup.objects.all()
    serializer = MeetupSerializer(meetups, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMeetup(request, pk):
    meetup = Meetup.objects.get(id=pk)
    serializer = MeetupSerializer(meetup, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getFavs(request):
    favorites = Meetup.objects.filter(isFavorite=True)
    serializer = MeetupSerializer(favorites, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createMeetup(request):
    data = request.data
    
    meetup = Meetup.objects.create(
        title=data['title'],
        description=data['description'],
        address=data['address'],
        image=request.FILES['image'],
        isFavorite=False
    )
    serializer = MeetupSerializer(meetup, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def modifyFav(request, pk):
    meetup = Meetup.objects.get(id=pk)
    meetup.isFavorite = not meetup.isFavorite
    meetup.save()
    serializer = MeetupSerializer(meetup, many=False)
    return Response(serializer.data)
