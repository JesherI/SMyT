# Generated by Django 5.0.6 on 2024-06-10 21:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Licence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('licence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module.licence', to_field='name')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('question_type', models.CharField(choices=[('MC', 'Multiple Choice'), ('TF', 'True/False')], max_length=2)),
                ('answerA', models.CharField(max_length=100)),
                ('answerB', models.CharField(max_length=100)),
                ('answerC', models.CharField(blank=True, max_length=100, null=True)),
                ('answerD', models.CharField(blank=True, max_length=100, null=True)),
                ('correct_answer', models.CharField(choices=[('A', 'Answer A'), ('B', 'Answer B'), ('C', 'Answer C'), ('D', 'Answer D')], max_length=1, null=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module.module', to_field='name')),
            ],
        ),
    ]
