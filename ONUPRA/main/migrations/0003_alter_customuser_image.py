# Generated by Django 4.0.1 on 2022-08-13 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]