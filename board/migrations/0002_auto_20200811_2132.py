# Generated by Django 3.1 on 2020-08-11 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]