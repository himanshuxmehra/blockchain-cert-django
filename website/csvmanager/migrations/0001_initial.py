# Generated by Django 3.1.2 on 2020-10-26 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='email')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='name')),
                ('university_name', models.CharField(max_length=200, null=True, verbose_name='university name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CSVFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('csv', models.FileField(null=True, upload_to='%Y/%m/%d/')),
                ('network', models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=60, null=True)),
                ('status', models.CharField(choices=[('Idle', 'Idle'), ('Processing', 'Processing'), ('Done', 'Done')], default='Idle', editable=False, max_length=60, null=True)),
                ('result_csv', models.FileField(default='', editable=False, null=True, upload_to='')),
                ('uploader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
