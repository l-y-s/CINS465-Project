"""
Url definition file to redistribute incoming URL requests to django
views. Search the Django documentation for "URL dispatcher" for more
help.

"""
from django.conf.urls import url, include
from web import customviews

# default evennia patterns
from evennia.web.urls import urlpatterns

# eventual custom patterns
custom_patterns = [
    url(r'profile', customviews.profilepage, name='profile'),
    url(r'stats', customviews.statspage, name='stats')
]

# this is required by Django.
urlpatterns = custom_patterns + urlpatterns
