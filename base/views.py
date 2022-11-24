from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe


from .models import *
from .models import Event
#from .forms import TodoForm
from .utils import Calendar

# Create your views here.

calendarsPages = [
    {'id': 1, 'name': 'School'},
    {'id': 2, 'name': 'Social'},
    {'id': 3, 'name': 'health'},
]

# todos = [
#{'id': 1, 'name': 'work on homework'},
#{'id': 2, 'name': 'workout'},
#{'id': 3, 'name': 'go to an event'},
# ]


def home(request):
    todos = Event.objects.all()
    context = {'calendars': calendarsPages, 'todos': todos}
    return render(request, 'base/templates/HomePage.html', context)

def login(request):
    context = {'login': login}
    return render(request, 'base/templates/Login.html', context)

def signup(request):
    context = {'signup': signup}
    return render(request, 'base/templates/SignUpPage.html', context)    


# def calendar(request, pk):
    # calendar = None
    # for i in calendars:
    # if i['id'] == int(pk):
    # calendar = i
    # context = {'calendar': calendar}
    # return render(request, 'base/templates/CalendarPage.html', context)'

def todo(request, pk):
    todo = Event.objects.get(id=pk)
    context = {'todo': todo}
    return render(request, 'base/templates/todo.html', context)


def addTask(request):
    form = TodoForms()

    if request.method == 'POST':
        form = TodoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/templates/todo_form.html', context)


class CalendarView(generic.ListView):
    model = Event
    template_name = 'base/templates/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()