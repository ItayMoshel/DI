from django.shortcuts import render
from .data import animals, families
from django.http import HttpResponse


# Create your views here.


def display_all_animals(request):
    return HttpResponse(animals)


def display_all_families(request):
    return HttpResponse(families)


def display_one_animal(request, animal_id):
    data = []
    if animals[animal_id] in animals:
        for key, value in animals[animal_id].items():
            data.append([f"{key}: {value}"])
        return HttpResponse(data)
    else:
        return HttpResponse("Wrong Id Value")


def display_animal_per_family(request, family_id):
    data = []
    for i in animals:
        if i["family"] == family_id:
            data.append(i)
    return HttpResponse(data)
