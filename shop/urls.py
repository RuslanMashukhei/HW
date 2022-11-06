from django.urls import path
from .views import greetings, ItemListView, DetailItemView
urlpatterns = [
    path('shop/greetings', greetings, name="greetings"),
    # path('shop/', list_item, name="list_item"),
    path('shop/', ItemListView.as_view(), name="list_item"),
    # path('shop/<int:item_id>/', detail_item, name="detail_item")
    path('shop/<int:pk>/', DetailItemView.as_view(), name="detail_item"),
]