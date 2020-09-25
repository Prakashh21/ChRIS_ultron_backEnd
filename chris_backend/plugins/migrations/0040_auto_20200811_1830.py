# Generated by Django 2.2.12 on 2020-08-11 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0039_auto_20200610_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plugin',
            name='documentation',
        ),
        migrations.RemoveField(
            model_name='plugin',
            name='title',
        ),
        migrations.AddField(
            model_name='pluginmeta',
            name='documentation',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='pluginmeta',
            name='title',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]