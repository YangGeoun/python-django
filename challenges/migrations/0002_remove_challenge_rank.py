# Generated by Django 4.2.6 on 2023-10-30 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='rank',
        ),
    ]
