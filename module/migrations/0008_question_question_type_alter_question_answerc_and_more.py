# Generated by Django 5.0.6 on 2024-06-03 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0007_question_correct_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('MC', 'Multiple Choice'), ('TF', 'True/False')], default='MC', max_length=2),
        ),
        migrations.AlterField(
            model_name='question',
            name='answerC',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='answerD',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(choices=[('A', 'Answer A'), ('B', 'Answer B'), ('C', 'Answer C'), ('D', 'Answer D')], max_length=1, null=True),
        ),
    ]