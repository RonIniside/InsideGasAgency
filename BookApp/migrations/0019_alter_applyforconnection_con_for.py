# Generated by Django 4.2.2 on 2023-08-14 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0018_remove_addcylinder_id_addcylinder_cylinder_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyforconnection',
            name='Con_for',
            field=models.CharField(max_length=20),
        ),
    ]
