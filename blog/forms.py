from django import forms
from django.forms import fields, widgets
from .models import Comment, Post    

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['auther','title','short_description','description','category','img']

    # def __init__(self,*args, **kwargs):
    #     super(PostForm,self).__init__(*args, **kwargs)
    #     self.fields['auther'].disabled=True


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post','user','budy']
