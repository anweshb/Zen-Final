# Generated by Django 2.2.6 on 2019-10-29 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='user',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='experience',
            new_name='exp',
        ),
    ]