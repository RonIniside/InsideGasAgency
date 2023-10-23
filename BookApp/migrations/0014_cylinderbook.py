# Generated by Django 4.2.2 on 2023-08-09 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0013_alter_addcylinder_cylinderimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CylinderBook',
            fields=[
                ('Booking_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Connection_no', models.CharField(max_length=20)),
                ('Type', models.CharField(max_length=20)),
                ('Price', models.IntegerField()),
                ('Payment_Mode', models.CharField(max_length=20)),
                ('Status', models.CharField(max_length=20)),
                ('Booking_date', models.DateField()),
            ],
        ),
    ]
