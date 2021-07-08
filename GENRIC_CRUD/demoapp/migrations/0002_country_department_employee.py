# Generated by Django 3.1.7 on 2021-06-20 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.AutoField(db_column='Country_id', primary_key=True, serialize=False)),
                ('country_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('did', models.AutoField(primary_key=True, serialize=False)),
                ('dname', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(blank=True, max_length=40, null=True)),
                ('adress', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
    ]
