from django import forms
from django.forms import ModelForm
from .models import Event
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class TodoForms(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

#class RegisterationForm(UserCreationForm):
 #   email = forms.EmailField(max_length=255)
    #firstName = forms.CharField(max_length=255)
    #lastName = forms.CharField(max_length=255)
    #phoneNum = forms.CharField(max_length=255)

  #  class Meta:
   #     model = User
        #fields = ('firstName', 'lastName', 'email', 'phoneNum', 'username', 'password1', 'password2')
    #    fields = ('email', 'username', 'password1', 'password2')

    #def clean_email(self):
     #   email = self.cleaned_date['email'].lower()

      #  try:
       #     account = User.objects.get(email=email)
        #except Exception as e:
         #   return email
        #raise forms.ValidationError("Email {email} is already in use.")

    #def clean_username(self):
     #   username = self.cleaned_date['username']

      #  try:
       #     account = User.objects.get(username=username)
        #except Exception as e:
         #   return username
        #raise forms.ValidationError("Username {username} is already in use.")

class SignUpForm(UserCreationForm):
    firstName = forms.CharField(
        max_length=100,
        widget = forms.TextInput(attrs={'class':'firstName', 'placeholder':'First Name'})
    )

    lastName = forms.CharField(
        max_length=100,
        widget = forms.TextInput(attrs={'class':'lastName', 'placeholder':'Last Name'})
    )

    email = forms.EmailField(
        max_length=150,
        widget = forms.TextInput(attrs={'class':'email', 'placeholder':'Email'})    
    )

    username = forms.CharField(
        widget = forms.TextInput(attrs={'class':'username', 'placeholder':'Username'})
    )

    password1 = forms.CharField(
        widget = forms.PasswordInput(attrs={'class':'pass', 'placeholder':'Password'})
    )

    password2 = forms.CharField(
        widget = forms.PasswordInput(attrs={'class':'pass', 'placeholder':'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'email', 'username', 'password1', 'password2')
