# Generated by Django 4.2 on 2023-11-01 00:47

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('beakjoon_nickname', models.CharField(blank=True, max_length=30, verbose_name='백준 닉네임')),
                ('beakjoon_rank', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='이메일')),
                ('username', models.CharField(max_length=30, verbose_name='이름')),
                ('is_staff', models.BooleanField(default=False, verbose_name='스태프 권한')),
                ('is_active', models.BooleanField(default=True, verbose_name='사용중')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='가입일')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('followings', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
