# Generated by Django 4.1.9 on 2023-07-18 18:34

import apps.core.utils.helpers
import apps.core.validators
import apps.users.manager
import django.core.validators
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
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, null=True, unique=True, verbose_name='username')),
                ('full_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='full name')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, verbose_name='email address')),
                ('profile_picture', models.ImageField(blank=True, upload_to=apps.core.utils.helpers.get_upload_path)),
                ('phone_number', models.CharField(error_messages={'unique': 'A user with that phone number already exists.'}, max_length=25, null=True, unique=True, validators=[apps.core.validators.validate_phone_number], verbose_name='phone number')),
                ('verification_code', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(100000), django.core.validators.MaxValueValidator(999999), django.core.validators.RegexValidator('^\\d{6}$', 'Enter a valid 6-digit number.')])),
                ('is_verified', models.BooleanField(default=False)),
                ('user_type', models.CharField(blank=True, choices=[('Employer', 'employer'), ('Jobseeker', 'Jobseeker')], max_length=25, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', apps.users.manager.UserManager()),
            ],
        ),
    ]
