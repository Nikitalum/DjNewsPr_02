from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Текст')
    date = models.DateTimeField('Дата')

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='News'
    )

    def __str__(self):
        return f'{self.title},{self.date},{self.text}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subscribers = models.ManyToManyField(User,related_name='categories')
                
    def __str__(self):
        return self.name.title()
    
class Subscriber(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )


class Post(models.Model):
    article = 'A'
    news = 'N'
    POSITIONS = [
        (article, 'статья'),
        (news, 'новость')
    ]
    type = models.CharField(max_length=1, choices=POSITIONS, default=news)
    date = models.DateTimeField('Дата')
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=225)
    text = models.TextField()

    def preview(self):
        preview=f'{self.text[:124]} ...'
        return preview

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles_list', kwargs={"pk": self.pk})


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


