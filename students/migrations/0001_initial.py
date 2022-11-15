# Generated by Django 3.2.12 on 2022-11-15 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students_assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_submitted', models.FileField(upload_to='')),
                ('submitted_on', models.DateTimeField()),
                ('marks_reci', models.TextField()),
                ('roll_number', models.TextField()),
                ('file_name', models.TextField()),
                ('assignments_id', models.TextField()),
            ],
        ),
    ]
