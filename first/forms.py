from django import forms

from first.models import Post, Comment, group

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        # fields = ('title', 'content')


class PostDeleteConfirmForm(forms.Form):
    check = forms.BooleanField(
        required=True, 
        label='你確定要刪除這篇文章嗎？',
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = "__all__"
        exclude = ("post",)

class commentDeleteConfirmForm(forms.Form):
    check = forms.BooleanField(
        required=True, 
        label='你確定要刪除這則留言嗎？',
    )

class GroupfForm(forms.ModelForm):
    class Meta:
        model = group
        fields = "__all__"
        # fields = ('title', 'content')

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }