# Generated by Django 4.0.4 on 2022-11-10 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_remove_type1_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='')),
                ('desc', models.TextField()),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.type1')),
            ],
        ),
    ]