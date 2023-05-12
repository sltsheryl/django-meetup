from rest_framework.serializers import ModelSerializer
from .models import Meetup

class MeetupSerializer(ModelSerializer):
    class Meta:
        model = Meetup
        fields = '__all__'
