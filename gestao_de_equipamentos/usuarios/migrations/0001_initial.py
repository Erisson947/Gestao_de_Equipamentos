# Generated by Django 4.2.11 on 2024-05-27 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import usuarios.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('registration', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('campus', models.CharField(default=None, max_length=4, null=True)),
                ('course', models.CharField(default=None, max_length=75, null=True)),
                ('full_name', models.CharField(max_length=200)),
                ('personal_email', models.EmailField(max_length=250, unique=True)),
                ('school_email', models.EmailField(max_length=250, unique=True)),
                ('academic_email', models.EmailField(max_length=250, unique=True)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('link_type', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=1)),
                ('date_of_birth', models.DateField()),
                ('photo1', models.URLField(max_length=600)),
                ('photo2', models.URLField(max_length=600)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', usuarios.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=254, unique=True)),
                ('email_type', models.CharField(db_column='type', max_length=15)),
                ('user', models.ForeignKey(db_column='user_registration', on_delete=django.db.models.deletion.CASCADE, related_name='emails', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
