# Generated by Django 5.0.6 on 2024-06-10 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=40)),
                ('first_lastname', models.CharField(max_length=40)),
                ('second_lastname', models.CharField(max_length=40)),
                ('admin', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('curp', models.CharField(max_length=18, unique=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
