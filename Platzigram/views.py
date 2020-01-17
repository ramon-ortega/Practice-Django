#Platzigram views.

#Django
from django.http import HttpResponse
from django.http import JsonResponse

#Utilities
from datetime import datetime
import json

def saludo(request):
    # Is only a greeting.
    return HttpResponse('Hi!, the Current time in server is {now}'.format(
        now=datetime.now().strftime("%b %d th %Y - %H:%M hrs")))

def sort_integers(requets):
    #Return a JSON response with sorted integers.
    numbers = [int(i) for i in requets.GET['numbers'].split(',')]
    #import pdb;pdb.set_trace()
    sortednumbers = sorted(numbers)
    return JsonResponse(sortednumbers, safe=False)

def other_sort_integers(requets):
    #Other form of sort_integers
    numbers = [int(i) for i in requets.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'Integers sorted successfully.',
    }
    return HttpResponse(json.dumps(
        data, indent=4),
        content_type='application/json'
    )

def say_hi(requets, name, age):
    #Is only a greeting.
    if age < 12:
        message = 'Im sorry {}, you cant stay here!'.format(name)
    else:
        message = 'Welcome {} '.format(name)
    return HttpResponse(message)