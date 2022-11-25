from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

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

#class Profile(models.Model):
 #   user = models.OneToOneField(User, on_delete=models.CASCADE)
  #  firstName = models.CharField(max_length=100, blank=True)
   # lastName = models.CharField(max_length=100, blank=True)
    #email = models.EmailField(max_length=150)
    
    #def __str__(self):
     #   return self.user.username

#@receiver(post_save, sender=User)
#def updateProfileSignal(sender, instance, created, **kwargs):
 #   try:
  #      instance.profile.save()
   # except ObjectDoesNotExist:
    #    Profile.objects.create(user=instance)
