# Generated by Django 2.1.4 on 2019-01-19 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divaDoc', '0002_disease_medicine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='dis',
        ),
        migrations.DeleteModel(
            name='disease',
        ),
        migrations.DeleteModel(
            name='medicine',
        ),
    ]
