# Generated by Django 4.1.3 on 2022-11-14 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_alter_assignments_file_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignments',
            name='posted_on',
            field=models.TextField(default='one'),
            preserve_default=False,
        ),
    ]