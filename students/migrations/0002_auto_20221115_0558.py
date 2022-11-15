# Generated by Django 3.2.12 on 2022-11-15 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students_assignment',
            name='file_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='students_assignment',
            name='file_submitted',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='students_assignment',
            name='marks_reci',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='students_assignment',
            name='submitted_on',
            field=models.DateTimeField(null=True),
        ),
    ]