# Generated by Django 3.1 on 2020-08-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20200811_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='comment',
        ),
        migrations.AlterField(
            model_name='post',
            name='password',
            field=models.BinaryField(max_length=500),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
