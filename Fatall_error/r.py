class Page_url:
    url = 'https://www.2gis.ru/countries/global/'
    city = ''

    # Генерация URL для парсинга страницы
    def __init__(self, city='blagoveshensk'):
        self.city = city
        self.url = self.url + city



def main():
    entry = Page_url('jjjjk')
    print(entry.city)





if __name__ == '__main__':
    main()