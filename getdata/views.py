from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("test pass!!!!!!!!")

def no(request):
    return HttpResponse("no route test pass!!!!!!")


def test(request):
    return HttpResponse("test2 pass successfully!!!!!")