"""Platzigram views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sort(request):
    """
    A Django view that returns the given numbers in a Json format and in orden.
    Returns:
        [Json]: Sorted list of the given numbers.
    """
    numbers = request.GET['numbers']
    list_numbers = list(numbers.split(",")) #divide los strings con comas y los almacena en una lista
    list_numbers = list(map(int, list_numbers)) #conveirte la lista de strings en enteros
    list_numbers.sort() #ordena la lista
    return HttpResponse(json.dumps(list_numbers)) #retorna json


def say_hi(request, name, age):
    """
    A Django view that create a personalized url path as the user's name.
    As well, greeting the user if successful.
    """
    if age < 12:
        message = "Sorry {}, Age must be over 12 years old to be allowed for view this page.".format(name)
    else:
        message = "Hello {}, wellcome to Platzigram!".format(name)
    return HttpResponse(message)
