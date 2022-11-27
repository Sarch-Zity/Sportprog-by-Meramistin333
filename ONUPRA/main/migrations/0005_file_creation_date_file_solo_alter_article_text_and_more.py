# Generated by Django 4.0.1 on 2022-11-03 05:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_image_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='solo',
            field=models.BooleanField(default=False, verbose_name='Только картинка'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='О чем вы хотите рассказать?'),
        ),
        migrations.AlterField(
            model_name='file',
            name='article',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.article'),
        ),
    ]