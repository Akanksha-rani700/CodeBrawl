# Generated by Django 3.0.4 on 2020-03-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participants',
            name='username2',
            field=models.CharField(default='TEST', max_length=20),
        ),
    ]