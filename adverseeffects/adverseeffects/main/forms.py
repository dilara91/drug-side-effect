from django import forms
from django.contrib.auth.models import User
from models import User, Blog, Drug, AdverseEffect, Tag, Comment
 
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        exclude = ('drugname', 'activeingredients')
        