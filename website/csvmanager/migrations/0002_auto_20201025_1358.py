# Generated by Django 3.1.2 on 2020-10-25 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfile',
            name='status',
            field=models.CharField(choices=[('Idle', 'Idle'), ('Processing', 'Processing'), ('Done', 'Done')], default='Idle', editable=False, max_length=60, null=True),
        ),
    ]
