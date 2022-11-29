from django.urls import path

from.views import json_message
urlpatterns = [
    path("", json_message, name="home"),
]