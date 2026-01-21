from django.shortcuts import render

from django.http import HttpResponse

def recipe_list(request):
    return HttpResponse("Recipes page")


# Create your views here.
