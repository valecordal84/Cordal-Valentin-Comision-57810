# Generated by Django 5.0.6 on 2024-07-09 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juegoscomprar',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
