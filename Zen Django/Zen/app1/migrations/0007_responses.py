# Generated by Django 2.2.6 on 2019-10-31 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.TextField()),
                ('question2', models.TextField()),
                ('question3', models.TextField()),
                ('timespent1', models.TimeField()),
            ],
        ),
    ]