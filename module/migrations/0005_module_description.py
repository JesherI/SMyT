# Generated by Django 5.1 on 2024-08-20 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0004_licence_letter'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
    ]
