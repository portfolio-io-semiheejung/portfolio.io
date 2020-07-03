from django import forms
from .models import Portfolio, Github, Skillkind, Skil, Color, Aboutme, Education, Experience, Project, Develop

class AboutmeForm(forms.ModelForm):
    job = forms.CharField(
        label='직종',
        widget=forms.TextInput(
            attr={
                'class': 'my-job form-control',
                'placeholder': '직종을 입력하세요.(15자 이내)',             
            }
        )
    )

    introduce = forms.CharField(
        label='직종',
        widget=forms.TextInput(
            attr={
                'class': 'my-introduce form-control',
                'placeholder': '직종을 입력하세요.',             
            }
        )
    )   
   
    class Meta:
        model = Aboutme
        fields = '__all__'

class DevelopForm(forms.ModelForm): 


    class Meta:
        model = Develop
        fields = '__all__'

class EducationForm(forms.ModelForm): 


    class Meta:
        model = Education
        fields = '__all__'

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

