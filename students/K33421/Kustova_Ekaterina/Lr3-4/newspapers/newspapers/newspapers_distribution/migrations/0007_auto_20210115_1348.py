# Generated by Django 3.1.2 on 2021-01-15 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspapers_distribution', '0006_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=0, max_length=200, verbose_name='Пароль'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(max_length=200, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, verbose_name='Имя пользователя'),
        ),
    ]
