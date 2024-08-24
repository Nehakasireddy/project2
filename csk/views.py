from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def msd(request):
    return HttpResponse('<h1><marquee>thala is a cool captain ,good  keeper and good batsman of team</marquee></h1>')
def raina(request):
    return render(request,'dhoni.html')
