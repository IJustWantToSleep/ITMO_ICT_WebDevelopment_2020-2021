# Generated by Django 3.1.2 on 2021-01-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspapers_distribution', '0004_print'),
    ]

    operations = [
        migrations.AddField(
            model_name='print',
            name='print_id',
            field=models.IntegerField(default=0, verbose_name='Номер печати'),
        ),
    ]