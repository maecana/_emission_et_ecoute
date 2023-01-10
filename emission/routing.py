from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/emit/(?P<space>\w+)/$', consumers.EmissionConsumer.as_asgi()),
]
