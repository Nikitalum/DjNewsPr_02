from django.db import models
from django.urls import reverse


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

    def __str__(self):
        return self.name.title()


class Post(models.Model):
    article = 'AR'
    news_post = 'NP'
    POST_TYPES = [
        (article, 'Статья'),
        (news_post, 'Новость')
    ]
    post_type = models.CharField(max_length=2, choices=POST_TYPES, default=news_post)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
