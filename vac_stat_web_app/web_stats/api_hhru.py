import re
import requests


class DataVacanciesFromHH:
    """Класс работы с API HH.ru"""

    def __get_full_vacancies__(self, text: str, date: str, count_vac: int) -> list:
        """Метод получения списка вакансий с полной информацией за конкретную дату

        :param date: Искомая дата
        :param count_vac: Количество вакансий (до 100)
        :return: Список вакансий с полной информацией
        """
        url = 'https://api.hh.ru/vacancies'
        return requests.get(url, dict(text=text,
                                      specialization=1,
                                      date_from=f"{date}T00:00:00",
                                      date_to=f"{date}T23:00:00",
                                      per_page=count_vac,
                                      page=1)).json()["items"]

    def get_data_vacancies(self, search_text: str, date: str, count_vac: int):
        """Метод получения списка вакансий только с необходимыми парами ключ:значение

        :param search_text: Текст для поиска нужной вакансии
        :param date: Искомая дата
        :param count_vac: Количество вакансий (до 100)
        :return: Список обработанных вакансий
        """
        data = self.__get_full_vacancies__(search_text, date, count_vac)
        result_list = []
        for vac in data:
            url_vac = f'https://api.hh.ru/vacancies/{vac["id"]}'
            resp = requests.get(url_vac).json()
            if resp['salary']:
                self.processing_data(resp, result_list)
        return result_list

    @staticmethod
    def processing_data(resp, result_list):
        """Метод обработки данных вакансии"""
        description = ' '.join(re.sub(re.compile('<.*?>'), '', resp['description'])
                               .strip()
                               .split())
        description = description[:500] + '...' if len(description) >= 100 else description
        result_list.append({'name': resp['name'],
                            'description': description,
                            'key_skills': ', '.join(map(lambda x: x['name'], resp['key_skills'])),
                            'employer': resp['employer']['name'],
                            'salary': f"{resp['salary']['from']} - {resp['salary']['to']} {resp['salary']['currency']}",
                            'area': resp['area']['name'],
                            'published_at': resp['published_at'][:10],
                            'alternate_url': resp['alternate_url']})
