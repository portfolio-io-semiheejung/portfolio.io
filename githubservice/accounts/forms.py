from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username','password1','password2','github_username')


class CustomUserChangeForm(UserChangeForm):
    username =  forms.CharField(
        widget=forms.TextInput(
            attrs={'title':'', 'readonly':'readonly'}
        ))
    class Meta:
        model = get_user_model()
        fields = ('username','github_username')
