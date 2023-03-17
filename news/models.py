from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField('Название', max_length=250)
    anons = models.CharField('Анонс', max_length=250)
    text = models.TextField('Текст')
    date = models.DateField('Дата')
    time = models.TimeField('Время')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'