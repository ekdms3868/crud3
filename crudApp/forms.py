from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'writer', 'body','image']

# CommentForm 작성
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']