# Generated by Django 4.1.5 on 2023-01-10 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_stats', '0004_rename_slr_by_cities_keyskillspageels_key_skills_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandpageels',
            name='csv',
            field=models.FileField(default=None, upload_to='upload_files/', verbose_name='Таблица динамики и количества вакансий по годам'),
        ),
        migrations.AddField(
            model_name='geographypageels',
            name='count_vac_table',
            field=models.FileField(default=None, upload_to='upload_files/', verbose_name='Таблица долей вакансий по городам'),
        ),
        migrations.AddField(
            model_name='geographypageels',
            name='slr_table',
            field=models.FileField(default=None, upload_to='upload_files/', verbose_name='Таблица уровня ЗП по городам'),
        ),
    ]
