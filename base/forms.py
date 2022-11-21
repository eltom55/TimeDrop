from django.forms import ModelForm
from .models import Event


class TodoForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
