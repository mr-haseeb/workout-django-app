# Generated by Django 2.0 on 2018-06-20 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='image',
            field=models.ImageField(blank=True, upload_to='planner/program/'),
        ),
    ]
