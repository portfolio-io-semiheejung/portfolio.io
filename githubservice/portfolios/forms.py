from django import forms
from .models import Usercontent, Skill, Project, Education,Experience

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
   
    develop_content1 = forms.CharField(
        label='develop life 1',
        widget=forms.TextInput(
            attrs={
                'class': 'my-develop_content1 form-control',
                'placeholder': '주요 프로젝트나 경력 1번을 입력하세요.',             
            }
        )
    )

    develop_content2 = forms.CharField(
        label='develop life 2',
        widget=forms.TextInput(
            attrs={
                'class': 'my-develop_content2 form-control',
                'placeholder': '주요 프로젝트나 경력 2번을 입력하세요.',             
            }
        )
    ) 

    develop_content3 = forms.CharField(
        label='develop life 3',
        widget=forms.TextInput(
            attrs={
                'class': 'my-develop_content3 form-control',
                'placeholder': '주요 프로젝트나 경력 3번을 입력하세요.',             
            }
        )
    ) 

    develop_content4 = forms.CharField(
        label='develop life 4',
        widget=forms.TextInput(
            attrs={
                'class': 'my-develop_content4 form-control',
                'placeholder': '주요 프로젝트나 경력 4번을 입력하세요.',             
            }
        )
    ) 

    develop_content5 = forms.CharField(
        label='develop life 5',
        widget=forms.TextInput(
            attrs={
                'class': 'my-develop_content5 form-control',
                'placeholder': '주요 프로젝트나 경력 5번을 입력하세요.',             
            }
        )
    ) 

    develop_content6 = forms.CharField(
        label='develop life 6',
        widget=forms.TextInput(
            attrs={
                'class': 'my-develop_content6 form-control',
                'placeholder': '주요 프로젝트나 경력을 입력하세요.',             
            }
        )
    )    

    all_skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),        
        widget=forms.CheckboxSelectMultiple()
    )



    class Meta:
        model = Usercontent
        #fields = [
        #    'job', 'introduce','develop_content1','develop_content2','develop_content3','develop_content4','develop_content5','develop_content6'
        #]
        #fields = '__all__'
        exclude =('user',)

<<<<<<< HEAD

class GithubForm(forms.ModelForm):
    class Meta:
        model = Github
=======
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        #exclude =('usercontent',)
        fields = '__all__'

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        #exclude =('usercontent',)
        fields = '__all__'


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        #exclude =('usercontent',)
>>>>>>> heejung
        fields = '__all__'