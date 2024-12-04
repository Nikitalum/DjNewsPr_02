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
       fields = 'title', 'text', 'date', 'category',


class NewsCrForm(forms.ModelForm):
   class Meta:
       model = Articles
       fields = 'title', 'text', 'date', 'category',
       def form_Valid(self):
           messages.success(request, "Your post has been successfully updated")
