# Generated by Django 3.1 on 2020-08-12 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_auto_20200812_0827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='reply',
        ),
        migrations.AddField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='board.post'),
        ),
    ]
