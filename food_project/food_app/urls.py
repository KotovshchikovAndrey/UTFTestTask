from django.urls import path
from food_app import views

urlpatterns = [
    path("", views.FoodListView.as_view(), name="food-list"),
]
