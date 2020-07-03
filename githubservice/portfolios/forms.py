from django import forms
from .models import Usercontent

#from .models import 

class UsercontentForm(forms.ModelForm):
    job = forms.CharField(
        label='직종',
        widget=forms.TextInput(
            attrs={
                'class': 'my-job form-control',
                'placeholder': '직종을 입력하세요.(15자 이내)',             
            }
        )
    )
    introduce = forms.CharField(
        label='소개',
        widget=forms.TextInput(
            attrs={
                'class': 'my-introduce form-control',
                'placeholder': '간략한 소개를 입력하세요.',             
            }
        )
    )   
    class Meta:
        model = Usercontent
        fields = '__all__'

