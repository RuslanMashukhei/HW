from django.urls import path
from .views import greetings, list_item, detail_item
urlpatterns = [
    path('shop/greetings', greetings, name="greetings"),
    path('shop/', list_item, name="list_item"),
    path('shop/<int:item_id>/', detail_item, name="detail_item")
]