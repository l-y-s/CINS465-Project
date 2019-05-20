# Code sourced from https://channels.readthedocs.io/en/stable/tutorial/part_2.html

from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]