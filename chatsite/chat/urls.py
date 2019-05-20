from django.conf.urls import url

from . import views

# Code sourced from https://channels.readthedocs.io/en/stable/tutorial/part_1.html
# and https://channels.readthedocs.io/en/stable/tutorial/part_2.html
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]