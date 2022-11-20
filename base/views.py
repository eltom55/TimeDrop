from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'HomePage.html')


def calendar(request):
    return render(request, 'CalendarPage.html')

#esfjl;ksafj;