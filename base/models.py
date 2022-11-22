from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateField()  # change back to datatimefield
    end_time = models.DateField()

    def __str__(self):
        return self.title
