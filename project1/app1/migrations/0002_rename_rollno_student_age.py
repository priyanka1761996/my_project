# Generated by Django 5.0 on 2024-01-09 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='rollno',
            new_name='age',
        ),
    ]