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
            if 'dirTitleBecauseNoPredictions' in p_dict:
                direct = p_dict['dirTitleBecauseNoPredictions']
                print('No buses to '+direct)
            else:
                dr = p.direction
                if dr != None:
                    dr_dict = dr.attrs
                    pred = dr.find_all('prediction')
                    for pe in pred:
                        pre_dict = dict(pe.attrs)
                        print('Bus to '+dr_dict['title']+' in '+str(pre_dict['seconds'])+' seconds.')


bus_update()
