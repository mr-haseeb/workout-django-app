# Generated by Django 2.0 on 2018-06-17 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BodyPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=100)),
                ('image', models.ImageField(upload_to='workout/bodyparts/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=100)),
                ('description', models.TextField(default='none', max_length=300)),
                ('image', models.ImageField(upload_to='workout/exercises/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('main_muscles', models.ManyToManyField(related_name='main_muscles', to='exercise.BodyPart')),
                ('other_muscles', models.ManyToManyField(blank=True, related_name='other_muscles', to='exercise.BodyPart')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('exercise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercise.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=100)),
                ('description', models.TextField(default='none', max_length=300)),
                ('type', models.CharField(choices=[('BU', 'Bulking'), ('CU', 'Cutting'), ('MA', 'Maintaining')], default='MA', max_length=2)),
                ('image', models.ImageField(upload_to='workout/routines/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.PositiveIntegerField()),
                ('kgs', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rest', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TrainDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('exercise_sets', models.ManyToManyField(to='exercise.ExerciseSet')),
            ],
        ),
        migrations.AddField(
            model_name='routine',
            name='train_days',
            field=models.ManyToManyField(to='exercise.TrainDay'),
        ),
        migrations.AddField(
            model_name='exerciseset',
            name='set',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercise.Set'),
        ),
    ]