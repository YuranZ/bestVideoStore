# Generated by Django 3.0.7 on 2020-06-10 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='show.Video'),
        ),
    ]
