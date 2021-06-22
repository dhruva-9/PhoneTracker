from django import http
from django.shortcuts import render
from .api import api

from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def testFun(request):
    number = request.POST.get('text')
    numLength = len(number)

    if numLength > 10:
        returnDict = {
            'error': "The number cant be more than 10 digits"
        }
        return render(request, 'resubmit.html', returnDict)

    else:
        response = api(number)

        if response == False:
            returnDict = {
                'number': number
            }

            return render(request, '404.html', returnDict)
            
        else:
            Carrier = response[0]
            Region = response[1]
            respDict = {
                'Carrier': Carrier,
                'number': number,
                'Region': Region
            }
            return render(request, 'result.html', respDict)
