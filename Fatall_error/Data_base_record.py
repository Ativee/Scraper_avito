from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


class Pars_param():
    url = 'https://2gis.ru/'
    sities = ''
    input_point = ''
    def __init__(self, sity):
        self.sities = sity

    def set_param(self, sity):
        pass

A = Pars_param('Blaga')
print('Значение переменной url обьекта А равно:', A.sities)

class Pars_param_2(Pars_param):
    url2 = 'ffdf'
    def __init__(self, url_pp2):
        self.url2 = url_pp2

B = Pars_param_2('url2')
print('Значение переменной url2 обьекта B равно:', B.url2, '\n','Значение переменной url обьекта B равно:', B.url)


# class Object(Pars_param):