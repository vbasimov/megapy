# Generated by Django 2.1.4 on 2019-01-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debtApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='debt',
            options={'verbose_name': 'Задолженность', 'verbose_name_plural': 'Задолженности'},
        ),
        migrations.AlterField(
            model_name='debt',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='debt',
            name='secondName',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
    ]