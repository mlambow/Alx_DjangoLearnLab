from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagWidget as Widget
from .models import Comment, Post

class TagWidget():
    def __init__(self, attrs=None):
        default_attrs = {'placeholder': 'Enter tags separated by commas'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {'tags': TagWidget()}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']