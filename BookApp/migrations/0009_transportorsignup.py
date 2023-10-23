# Generated by Django 4.2.2 on 2023-08-03 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0008_delete_transportor'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransportorSignUp',
            fields=[
                ('t_id', models.IntegerField(primary_key=True, serialize=False)),
                ('t_name', models.CharField(max_length=20)),
                ('t_address', models.CharField(max_length=20)),
                ('t_gender', models.CharField(max_length=10)),
                ('t_age', models.IntegerField()),
                ('t_phone', models.IntegerField()),
                ('t_location', models.CharField(max_length=20)),
                ('t_VehicleNo', models.CharField(max_length=20)),
                ('t_VehicleType', models.CharField(max_length=20)),
                ('t_idproof', models.FileField(upload_to='GasBooking/media/TransportProff')),
                ('t_email', models.EmailField(max_length=20)),
                ('t_password', models.CharField(max_length=20)),
                ('t_joined_date', models.DateField()),
                ('t_is_activated', models.BooleanField()),
            ],
        ),
    ]
