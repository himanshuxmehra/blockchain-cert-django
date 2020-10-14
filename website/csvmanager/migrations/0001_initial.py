# Generated by Django 3.1.2 on 2020-10-14 11:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('university_name', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CSVFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('csv', models.FileField(null=True, upload_to='%Y/%m/%d/')),
                ('network', models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=60, null=True)),
                ('status', models.CharField(choices=[('Idle', 'Idle'), ('Processing', 'Processing'), ('Done', 'Done')], max_length=60, null=True)),
                ('uploader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='csvmanager.user')),
            ],
        ),
    ]
