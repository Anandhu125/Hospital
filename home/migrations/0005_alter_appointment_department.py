# Generated by Django 4.2.3 on 2023-08-01 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='department',
            field=models.CharField(max_length=50),
        ),
    ]
