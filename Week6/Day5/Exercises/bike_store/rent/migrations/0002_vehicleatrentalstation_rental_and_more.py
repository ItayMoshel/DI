# Generated by Django 4.1.4 on 2023-08-17 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleatrentalstation',
            name='rental',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rent.rental'),
        ),
        migrations.AddField(
            model_name='vehicleatrentalstation',
            name='rental_station',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='rent.rentalstation'),
        ),
    ]
