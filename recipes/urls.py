from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.recipe_list, name="recipes"),
    path("add/", views.add_recipe, name="add_recipe"),
]
