from django.db import models


# Create your models here.
class Register(models.Model):
    log_in = models.CharField('Логин', max_length=250)
    password = models.CharField('Пароль', max_length=250)

    def __str__(self):
        return self.log_in

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователя'