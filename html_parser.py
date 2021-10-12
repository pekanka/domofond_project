from bs4 import BeautifulSoup as bs
import pandas as pd
import pymysql
import requests
import re
import numpy as np
import os
from geopy.geocoders import Nominatim as gpy
import json
import csv
from sqlalchemy import create_engine

def pars(fl):
    fl = bs(requests.get(fl).text, 'html.parser')
    try:
        dct = {}
        prd = {}
        for i in list(fl.find_all(['span', 'div'], text='Квартира')[-1].find_parents()[1]):
            prd[re.search(r'.{1,25}[^:]', list(i)[0].text)[0]] = list(i)[-1].text

        cl = re.search(r'location__address\w{1,30}|location__text\w{1,30}', fl.prettify())[0]
        dct['address'] = fl.find_all(['div', 'h5', 'p'], class_ = cl)[0].text
        if re.search(r'information__metro__\w{1,30}', fl.prettify()) != None:
            dct['metro'] = ' '.join(list(fl.find_all('div', class_ = re.search(r'information__metro__\w{1,30}', fl.prettify())[0])[0])[-1].split(' ')[0:-2])
            dct['mt_dist'] = float(list(fl.find_all('div', class_ = re.search(r'information__metro__\w{1,30}', fl.prettify())[0])[0])[-1].split(' ')[-2])
            if list(fl.find_all('div', class_ = re.search(r'information__metro__\w{1,30}', fl.prettify())[0])[0])[-1].split(' ')[-1] == 'км':
                dct['mt_dist'] *= 1000
        else:
            dct['metro'] = np.NaN
            dct['mt_dist'] = np.NaN
        if prd['Комнаты'] == 'Студия':
            prd['Комнаты'] = 1
        elif prd['Комнаты'] == '> 9':
            prd['Комнаты'] = 10
        if re.findall(r'description__description___\w{1,10}', fl.prettify()) != []:
            prk = fl.find_all(['div', 'span'], class_ = re.findall(r'description__description___\w{1,10}', fl.prettify()))[-1].text
            if re.findall('[пП]арк\w', prk) != []:
                dct['parking'] = True
            else:
                dct['parking'] = False
        else: dct['parking'] = np.NaN
        dct['rooms'] = int(prd['Комнаты'])
        dct['floor_bld'] = int(prd['Этаж'].split('/')[1])
        dct['floor'] = int(prd['Этаж'].split('/')[0])
        dct['square'] = float(prd['Площадь'][:-2])
        dct['price_p_m'] = float(''.join(prd['Цена за м²'][:-2].split(' ')))
        dct['price'] = float(''.join(prd['Цена'][:-2].split(' ')))
    except:
        return {}
    return dct

#print(pars('https://www.domofond.ru/2-komnatnaya-kvartira-v-arendu-moskva-2425453201'))
