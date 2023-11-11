# Generated by Django 4.2.6 on 2023-11-10 21:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('problem_num', models.IntegerField()),
                ('rank', models.CharField(max_length=5)),
                ('solved_users', models.ManyToManyField(related_name='solved_problems', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ProblemClass_num', models.IntegerField(blank=True)),
                ('problems', models.ManyToManyField(related_name='classes', to='algorithms.problem')),
            ],
        ),
    ]
