from django.shortcuts import render
from django.http import HttpResponse


def recipe_list(request):
    return HttpResponse("Recipes page")

from django.shortcuts import render

def add_recipe(request):
    return render(request, "recipes/add_recipe.html")


