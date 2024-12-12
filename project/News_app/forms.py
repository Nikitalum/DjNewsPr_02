from django import forms
from .models import Articles
from django.contrib import messages


class ArticlesForm(forms.ModelForm):
   class Meta:
       model = Articles
       fields = '__all__'


class ArticlesCrForm(forms.ModelForm):
   class Meta:
       model = Articles
       fields = 'title', 'text', 'date',


class NewsCrForm(forms.ModelForm):
   class Meta:
       model = Articles
       fields = 'title', 'text', 'date',

