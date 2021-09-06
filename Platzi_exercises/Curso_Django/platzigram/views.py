# view example for django
from django.http import HttpResponse
from datetime import datetime
import json
#import pdb; pdb.set_trace()

def hello_world(request):
    """
    A Django view that prints 'Hello, world!'
    """
    now = str(datetime.now().strftime('%Y-%m-%d %H:%M'))
    return HttpResponse('Hello user! Current server time is {}'.format(now))

def sorted(request):
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
