# Generated by Django 4.1.6 on 2023-02-19 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_competition_amount_of_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='amount_of_users',
        ),
    ]