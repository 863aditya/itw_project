# Generated by Django 3.2.12 on 2022-11-15 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univworks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='username',
            field=models.TextField(default=5),
            preserve_default=False,
        ),
    ]
