# Generated by Django 4.0.1 on 2022-11-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_file_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='img/', verbose_name='Изображение'),
        ),
    ]