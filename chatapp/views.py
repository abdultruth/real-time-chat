from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required




from .models import Room

# Create your views here.
def index(request) -> str:
    return render(request, "chatapp/index.html")


@login_required(login_url='login')
def room(request, room_name) -> str:
    if request.user:
        room = Room.objects.get_or_create(name=room_name)
        return render(request, "chatapp/room.html", {"room_name": room_name})
    else:
        return redirect('login')
