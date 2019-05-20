from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Code sourced from https://channels.readthedocs.io/en/stable/tutorial/part_1.html
# and https://channels.readthedocs.io/en/stable/tutorial/part_2.html
def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })