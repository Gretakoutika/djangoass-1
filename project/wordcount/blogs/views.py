from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import operator
def drinks(requests):
    return HttpResponse('<h2> Drink water</h2')
def foods(requests):
    return HttpResponse('<h2>Dont eat junk food</h2>')
