from rest_framework import viewsets
from .models import Room
from .serializers import ReadRoomSerializer


class Roomviewset(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = ReadRoomSerializer
