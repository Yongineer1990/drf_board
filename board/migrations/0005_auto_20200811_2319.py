# Generated by Django 3.1 on 2020-08-11 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20200811_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='password',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='password',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='reply',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
