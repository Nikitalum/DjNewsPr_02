from django.db import models


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

