from django.shortcuts import render
from django.utils import timezone

# Create your views here.


import datetime, time, requests, re, os
import bs4



cwd = os.getcwd()
routeReg = re.compile(r'routeTitle="(\d+)"')


def bus_update():
    #stops = Stop.objects.all()
    #for s in stops:
        path = 'B:\\Users\\Eric\\Documents\\Coding\\psychic-succotash\\bus\\publicXMLFeed.xml'
        xmlf = open(path, 'r')
        xml = xmlf.read()
        soup = bs4.BeautifulSoup(xml, 'xml')
        preds = soup.find_all('predictions')
        for p in preds:
            p_dict = dict(p.attrs)
            print(p_dict)

bus_update()
