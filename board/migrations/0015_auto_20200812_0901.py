# Generated by Django 3.1 on 2020-08-12 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0014_auto_20200812_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='board.post'),
        ),
    ]
