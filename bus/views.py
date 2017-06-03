from django.shortcuts import render
from django.utils import timezone

# Create your views here.

import main, crawler
import datetime, time, requests, re, os
import bs4

from .models import File, Route, Stop, Prediction

cwd = os.getcwd()
routeReg = re.compile(r'routeTitle="(\d+)"')

def mode():
    #toggles mode based on time and day
    now = datetime.datetime.now(EST())
    wday = now.strftime('%w')
    h = now.strftime('%p')
    #print(wday)
    #print(h)
    if (wday == '1' or wday == '2' or wday == '3' or wday == '4' or wday == '5') and h == 'AM':
        mode = 1
    else:
        mode = 2
    return mode

def grabber(stop):
    x = 0
    now = timezone.now()
    feed = requests.get('http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=mbta&stopId=' + stop)
    if feed.status_code == requests.codes.ok:
        f_path = cwd+'/buslog/bus-'+str(stop)+strftime('%m-%d-%H:%M', now)+'.xml'
        xml = open(f_path, 'w')
        xml.write(feed.text)
        xml.close()
        f = File(path=f_path)
        f.save
    return f_path

def bus_update(request):
    stops = Stop.objects.all()
    for s in stops:
        path = grabber(s.stop_tag)
        xmlf = open(path, 'r')
        xml = xmlf.read()
        soup = bs4.BeautifulSoup(xml, 'xml')
        preds = soup.find_all('predictions')
        for p in preds:




def bus(request)
    return render(request, 'bus/bus.html', context)
