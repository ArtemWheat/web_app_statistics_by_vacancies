# Generated by Django 4.1.5 on 2023-01-09 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_stats', '0002_demandpageels_geographypageels_keyskillspageels_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyskillspageels',
            name='slr_by_cities',
            field=models.ImageField(upload_to='stats_img/', verbose_name='Топ 10 навыков'),
        ),
    ]