# Generated by Django 4.0.4 on 2022-11-07 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type1',
            name='desc',
        ),
    ]
