# Generated by Django 5.0.6 on 2024-05-27 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0002_licence_remove_module_license_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licence',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='licence',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='licence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='module.licence', to_field='name'),
        ),
    ]