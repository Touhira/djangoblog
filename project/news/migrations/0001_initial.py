# Generated by Django 4.0.1 on 2022-01-05 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('short_text', models.CharField(max_length=50, verbose_name='Краткое опимание')),
                ('full_text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(default=None, upload_to='', verbose_name='Картинки')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
