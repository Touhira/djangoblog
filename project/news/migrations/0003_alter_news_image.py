# Generated by Django 4.0.1 on 2022-01-05 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default=None, upload_to='main/static/media/anonymous_mask.png', verbose_name='Картинки'),
        ),
    ]
