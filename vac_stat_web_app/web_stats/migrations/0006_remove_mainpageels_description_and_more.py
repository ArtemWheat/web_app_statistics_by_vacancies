# Generated by Django 4.1.5 on 2023-01-13 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_stats', '0005_demandpageels_csv_geographypageels_count_vac_table_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainpageels',
            name='description',
        ),
        migrations.AddField(
            model_name='mainpageels',
            name='description1',
            field=models.TextField(default=None, verbose_name='Описание 1'),
        ),
        migrations.AddField(
            model_name='mainpageels',
            name='description2',
            field=models.TextField(default=None, verbose_name='Описание 2'),
        ),
        migrations.AddField(
            model_name='mainpageels',
            name='description3',
            field=models.TextField(default=None, verbose_name='Описание 3'),
        ),
        migrations.AddField(
            model_name='mainpageels',
            name='heading1',
            field=models.CharField(default=None, max_length=100, verbose_name='1-й заголовок'),
        ),
        migrations.AddField(
            model_name='mainpageels',
            name='heading2',
            field=models.CharField(default=None, max_length=100, verbose_name='2-й заголовок'),
        ),
        migrations.AddField(
            model_name='mainpageels',
            name='heading3',
            field=models.CharField(default=None, max_length=100, verbose_name='1-й заголовок'),
        ),
        migrations.AlterField(
            model_name='mainpageels',
            name='image',
            field=models.ImageField(default=None, upload_to='vac_img/', verbose_name='Изображение'),
        ),
    ]