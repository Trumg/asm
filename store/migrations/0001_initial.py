# Generated by Django 4.1.3 on 2023-01-03 10:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativities_name', models.CharField(max_length=100)),
                ('additional_comments', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('destination', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('activities_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.expenses')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.trip')),
            ],
        ),
    ]
