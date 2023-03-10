# Generated by Django 4.1.3 on 2023-01-03 10:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_ativities_name_expenses_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenses',
            old_name='name',
            new_name='activitites',
        ),
        migrations.AddField(
            model_name='expenses',
            name='trip',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='store.trip'),
        ),
        migrations.AddField(
            model_name='trip',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
