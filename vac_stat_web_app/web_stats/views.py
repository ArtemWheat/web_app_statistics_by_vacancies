import datetime

from django.shortcuts import render
from .api_hhru import DataVacanciesFromHH
from .models import MainPageEls, DemandPageEls, GeographyPageEls, KeySkillsPageEls
from .csv_converter import get_list_dicts_from_csv


def home(request):
    data = list(MainPageEls.objects.filter(draft=False))[0]
    return render(request, 'web_stats/main.html', {'data': data})


def demand(request):
    data = list(DemandPageEls.objects.filter(draft=False))[0]
    table1 = get_list_dicts_from_csv(data.csv.file.name)
    titles = list(table1[0].keys())
    return render(request, 'web_stats/demand.html', {'data1': data,
                                                     'table1': table1,
                                                     'titles': titles})


def geography(request):
    data = list(GeographyPageEls.objects.filter(draft=False))[0]
    table2 = get_list_dicts_from_csv(data.slr_table.file.name)
    titles2 = list(table2[0].keys())
    table3 = get_list_dicts_from_csv(data.count_vac_table.file.name)
    titles3 = list(table3[0].keys())
    return render(request, 'web_stats/geography.html', {'data2': data,
                                                        'table2': table2,
                                                        'table3': table3,
                                                        'titles2': titles2,
                                                        'titles3': titles3})


def key_skills(request):
    data = list(KeySkillsPageEls.objects.filter(draft=False))[0]
    return render(request, 'web_stats/key_skills.html', {'data4': data})


def vacancies(request):
    date = ''
    data = {}
    if request.GET != {}:
        date = request.GET['date']
        data = DataVacanciesFromHH().get_data_vacancies('C#', date, 10)
    date_now = datetime.datetime.date(datetime.datetime.now()).strftime("%Y-%m-%d")
    return render(request, 'web_stats/vacancies.html', {'data3': data,
                                                        'date_now': date_now})
