from django.shortcuts import HttpResponse
import operator
from django.shortcuts import render
def mhome(requests):
    return render(requests,'calc/mhome.html') 
def home(requests):
    return render(requests,'calc/home.html')
def calc(requests):
    text=requests.GET['expr']
    x=eval(text)
    return render(requests,'calc/calculator.html',{'ans':x,'text':text})

# Create your views here.
