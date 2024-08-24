from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def virat(request):
    return HttpResponse('<h1><marquee>virat is a  king of cricket</marquee></h1>')
def adb(request):
    return render(request,'adb.html')