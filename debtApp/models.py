from django.db import models

class Debt(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Имя')
    secondName = models.CharField(max_length = 100, verbose_name = 'Фамилия')
    debtValue = models.FloatField(verbose_name = 'Задолженность')

    def __str__(self):
        return self.name + ' ' +self.secondName

    class Meta:
        verbose_name = 'Задолженность'
        verbose_name_plural = 'Задолженности'
        ordering = ['secondName', 'name']
