from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def rohit(request):
    return render(request,'rohit.html')
def hardik(request):
    return HttpResponse('<h1> hardik is good bowler and batsman</h1>')