# Generated by Django 3.0.7 on 2020-06-13 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0005_video_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Видео', 'verbose_name_plural': 'Много видео'},
        ),
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name='Лайки'),
        ),
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(help_text='Слаг должен быть уникальным', unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='video',
            name='urls',
            field=models.URLField(verbose_name='УРЛ'),
        ),
    ]