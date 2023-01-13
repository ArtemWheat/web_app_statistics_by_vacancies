import csv


def get_list_dicts_from_csv(file_path: str):
    with open(file_path, encoding='utf-8-sig') as f:
        return [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]


if __name__ == '__main__':
    a = get_list_dicts_from_csv(
        'C:/Users/lenovo/PycharmProjects/vac_stat_web_app/vac_stat_web_app/media/upload_files/stat_by_year.csv')
    pass
