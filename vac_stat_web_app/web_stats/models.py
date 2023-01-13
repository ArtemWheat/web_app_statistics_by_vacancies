from django.db import models


class MainPageEls(models.Model):
    title = models.CharField("Название профессии", max_length=100)
    heading1 = models.CharField("1-й заголовок", max_length=100, default=None)
    description1 = models.TextField("Описание 1", default=None)
    heading2 = models.CharField("2-й заголовок", max_length=100, default=None)
    description2 = models.TextField("Описание 2", default=None)
    heading3 = models.CharField("1-й заголовок", max_length=100, default=None)
    description3 = models.TextField("Описание 3", default=None)
    image = models.ImageField("Изображение", upload_to="vac_img/", default=None)
    draft = models.BooleanField("Черновик", default=False)


class DemandPageEls(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    slr_by_year = models.ImageField("Динамика ЗП по годам", upload_to="stats_img/")
    count_vac_by_year = models.ImageField("Количество вакансий по годам", upload_to="stats_img/")
    csv = models.FileField("Таблица динамики и количества вакансий по годам", upload_to="upload_files/", default=None)  # TODO закинуть валидаторы
    description_1 = models.TextField("Описание рисунка 1", default=None)
    description_2 = models.TextField("Описание рисунка 2", default=None)
    description_3 = models.TextField("Описание рисунка 3", default=None)
    draft = models.BooleanField("Черновик", default=False)


class GeographyPageEls(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    slr_by_cities = models.ImageField("Динамика ЗП по городам", upload_to="stats_img/")
    count_vac_by_cities = models.ImageField("Количество вакансий по городам", upload_to="stats_img/")
    slr_table = models.FileField("Таблица уровня ЗП по городам", upload_to="upload_files/", default=None)  # TODO закинуть валидаторы
    count_vac_table = models.FileField("Таблица долей вакансий по городам", upload_to="upload_files/", default=None)  # TODO закинуть валидаторы
    draft = models.BooleanField("Черновик", default=False)


class KeySkillsPageEls(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    key_skills_img = models.ImageField("Топ 10 навыков", upload_to="stats_img/")
    draft = models.BooleanField("Черновик", default=False)
