from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CalendarIcon(models.Model):
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    # host = 
    # topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    start_time = models.DateField()  # change back to datatimefield
    end_time = models.DateField()
    #calendarIcon = models.ForeignKey(CalendarIcon, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
