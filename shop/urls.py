from django.urls import path
from .views import greetings
urlpatterns = [
    path('shop/greetings', greetings, name="greetings"),
]