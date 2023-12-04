from django.shortcuts import render


from .models import Room

# Create your views here.
def index(request):
    return render(request, "chatapp/index.html")


def room(request, room_name) -> str:
    room = Room.objects.get_or_create(name=room_name)
    if room:
        return render(request, "chatapp/room.html", {"room_name": room_name})
