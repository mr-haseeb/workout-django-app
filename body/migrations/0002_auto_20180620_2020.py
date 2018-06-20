# Generated by Django 2.0 on 2018-06-20 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muscle',
            name='image',
            field=models.ImageField(blank=True, upload_to='body/muscles/'),
        ),
        migrations.AlterField(
            model_name='musclegroup',
            name='image',
            field=models.ImageField(blank=True, upload_to='body/muscle_groups/'),
        ),
    ]
