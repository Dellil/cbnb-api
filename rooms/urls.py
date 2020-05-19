from django.urls import path
from .views import ListRoomsView, SeeRoomView


app_name = "rooms"

urlpatterns = [
    path("list/", ListRoomsView.as_view(), name="list"),
    path("<int:pk>/", SeeRoomView.as_view(), name="see")
]
