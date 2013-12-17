#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
#from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
from urlparse import urljoin

# Открываем html 
html_doc = urlopen('http://www.avito.ru/sankt-peterburg/kvartiry/prodam/1-komnatnye/vtorichka?metro_id=183&pmax=4000000&pmin=3000000&f=566_5827').read()
soup = BeautifulSoup(html_doc)

# Функция для преобразования ссылок
def make_links_absolute(soup, url):
    for tag in soup.findAll('a', href=True):
        tag['href'] = urljoin(url, tag['href'])
    return

# Загрузим все картинки к объявлениям
for tag in soup.findAll('img'):
    if tag.has_key('data-srcpath'):
        tag['src'] = tag['data-srcpath']   


make_links_absolute(soup, 'http://www.avito.ru')

# Выбираем нужный блок
div=soup.find('div', 'b-catalog-table')


# Сделаем файл и запишем в него результат
f=open('result.html', 'w')
print >> f, '<meta charset="utf-8"><title>Озерки</title><link rel="stylesheet" href="result.css" type="text/css" media="screen" /><h1>Озерки, вторичка, 3 000 000 - 4 000 000</h1><br /><br />', div
f.close