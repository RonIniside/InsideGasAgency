# Generated by Django 4.2.2 on 2023-08-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0014_cylinderbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='cylinderbook',
            name='Transportor_Name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='cylinderbook',
            name='Transportor_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cylinderbook',
            name='Transportor_phone',
            field=models.IntegerField(default=0),
        ),
    ]
