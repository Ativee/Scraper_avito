from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

"""
Парсинг сайта 2ГИС для составления базы данных огранизаций 

Алгоритм извлечения данных:

1. Парсинг первой страницы сайта для составления
    - рубрикатора
    - списка городов
    
2. Структура извлекаемых данных:
    - Город
    - Наименование огранизации
    - Номер телефона
    - Адресс
    - E-mail
    - Сайт
    - Смежные рубрики
    - Режим работы

    
3. Запись экземпляра класса в базу данных.
4. Потроение API для работы с базой данных.


Алгоритм отслеживания изменений и тенденций:

1. Проверка количества организаций по рубрикам
2. Сводка открывшихся и закрывшихся организаций
3. Сводка организаций проводящих рекламную компанию


"""

# Класс
class Main_page:
    url = 'https://www.2gis.ru/'
    city = ''


    def set(self, city):
        self.city = str(city)
        base_region = self.url + str(base)


    def dfffd(self):
        self.dfdf = dfdfd



class Rec_DB



class

amur = Page_html()
amur.set('blaga')

print(amur.base_region)




