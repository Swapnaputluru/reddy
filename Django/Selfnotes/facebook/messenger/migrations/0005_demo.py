# Generated by Django 3.2.5 on 2022-02-18 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0004_remove_address_pincode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
                ('higher_education', models.CharField(max_length=20)),
                ('passedout_year', models.IntegerField()),
            ],
        ),
    ]
