from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer


class ListRoomsView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

# FBV
# @api_view(["GET"])
# def list_rooms(request):
#     rooms = Room.objects.all()
#     serialized_rooms = RoomSerializer(rooms, many=True)

#     return Response(data=serialized_rooms.data)
