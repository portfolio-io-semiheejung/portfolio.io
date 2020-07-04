from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('user','like_users',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '댓글을 작성해주세요',             
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)
