from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("content",)
        widgets = {"content": forms.Textarea(attrs={"rows": 3, "placeholder": "What's on your mind?", "maxlength": 2000})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        widgets = {"content": forms.TextInput(attrs={"placeholder": "Write a comment...", "maxlength": 500})}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "location", "website")
        widgets = {"bio": forms.Textarea(attrs={"rows": 3}), "location": forms.TextInput(), "website": forms.URLInput()}
