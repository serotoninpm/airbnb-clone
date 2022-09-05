# Generated by Django 2.2.5 on 2022-08-28 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_auto_20220710_0254'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.Reservation')),
            ],
            options={
                'verbose_name': 'Booked Day',
                'verbose_name_plural': 'Booked Days',
            },
        ),
    ]
