# Generated by Django 5.0.2 on 2024-02-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='slug',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
