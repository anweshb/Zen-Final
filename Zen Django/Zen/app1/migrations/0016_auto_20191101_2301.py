# Generated by Django 2.2.6 on 2019-11-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_auto_20191101_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responses1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.TextField(default='')),
                ('timespent1', models.TextField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Responses2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question2', models.TextField(default='')),
                ('timespent2', models.TextField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Responses3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question3', models.TextField(default='')),
                ('timespent3', models.TextField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Responses4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question4', models.TextField(default='')),
                ('timespent4', models.TextField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Responses5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question5', models.TextField(default='')),
                ('timespent5', models.TextField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Responses6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question6', models.TextField(default='')),
                ('timespent6', models.TextField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Responses7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question7', models.TextField(default='')),
                ('timespent7', models.TextField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Responses8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question8', models.TextField(default='')),
                ('timespent8', models.TextField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Responses9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question9', models.TextField(default='')),
                ('timespent9', models.TextField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Responses',
        ),
    ]
