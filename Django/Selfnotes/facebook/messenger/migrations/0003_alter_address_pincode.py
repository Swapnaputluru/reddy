# Generated by Django 3.2.5 on 2022-02-18 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.IntegerField(max_length=6),
        ),
    ]
