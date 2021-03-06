# Generated by Django 3.2.9 on 2022-01-09 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Марка авто')),
                ('description', models.CharField(max_length=5000, verbose_name='Описание')),
                ('year', models.IntegerField(default=2020, verbose_name='Год выпуск')),
                ('doors', models.IntegerField(verbose_name='Количество дверей')),
                ('seats', models.IntegerField(verbose_name='Количество мест')),
                ('lugage', models.CharField(max_length=255, verbose_name='Багаж')),
                ('transmission', models.CharField(max_length=255, verbose_name='Трансмиссия')),
                ('minimum_age', models.IntegerField(verbose_name='Возвраст')),
                ('image', models.ImageField(upload_to='vehicles/', verbose_name='Фото авто')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
    ]
