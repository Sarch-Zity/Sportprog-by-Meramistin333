# Generated by Django 4.0.1 on 2022-11-27 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_customuser_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='soft',
        ),
    ]
