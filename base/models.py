from django.db import models

# Create your models here.


class CalendarIcon(models.Model):
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateField()  # change back to
    end_time = models.DateField()
    #calendarIcon = models.ForeignKey(CalendarIcon, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
