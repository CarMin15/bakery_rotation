# Generated by Django 2.0.6 on 2018-07-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baking_rotation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakingslot',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]