# Generated by Django 5.0 on 2024-02-20 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tourcode', models.CharField(max_length=10, unique='True')),
                ('tourname', models.CharField(max_length=30)),
                ('tourpackage', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=35)),
            ],
            options={
                'db_table': 'package_table',
            },
        ),
    ]
