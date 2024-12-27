from django import forms
from .models import Articles, Post
from django.contrib import messages


class ArticlesForm(forms.ModelForm):
   class Meta:
       model = Articles
       fields = '__all__'


class ArticlesCrForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = 'title', 'text', 'date', 'category'


class NewsCrForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = 'title', 'text', 'date',

