# Generated by Django 5.0.6 on 2024-06-21 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('module', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='module.module'),
        ),
    ]
