# Generated by Django 4.2.2 on 2023-09-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0027_cylinderbook_delivered_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=15)),
                ('Password', models.CharField(max_length=15)),
            ],
        ),
    ]
