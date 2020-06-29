from django import forms
from .models import User
from django.contrib.auth import get_user_model

class UserForm(forms.Form):
    
    class Meta:
        model = get_user_model()
        fields = '__all__'