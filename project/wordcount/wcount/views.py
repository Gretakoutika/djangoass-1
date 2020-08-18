from django.shortcuts import render
from django.shortcuts import HttpResponse
import operator
def home(requests):
    return HttpResponse('<h1> This is the first page</h1>')
def about(requests):
    return HttpResponse('<h1> ABOUT </h1><ul><li>K.Gretha</li><li> 1602-18-737-069</li></ul>')
def hobbies(requests):
    return HttpResponse('<h1> Hobbies</h1><ol><li>Singing</li><li>Dancing</li></ol>')
