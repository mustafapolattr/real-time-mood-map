from django.urls import re_path
from ..consumers.mood_consumer import MoodConsumer

websocket_urlpatterns = [
    re_path(r"ws/moods/$", MoodConsumer.as_asgi()),
]