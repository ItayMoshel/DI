# Generated by Django 4.2.4 on 2023-08-15 02:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]