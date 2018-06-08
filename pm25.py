#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sys, urllib, urllib2, json
import time
sys.path.append('/home/pi/SAKS-SDK')
from sakshat import SAKSHAT

#Declare the SAKS Board
SAKS = SAKSHAT()

weather_url = 'https://free-api.heweather.com/s6/air/now?location=CN101010100&key=687dce4e572d4b549bf43527fa2067fa'

def get_pm25():
    global weather_url
    req = urllib2.Request(weather_url)
    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        weatherJSON = json.JSONDecoder().decode(content)
        # print(weatherJSON)
        try:
            if weatherJSON['HeWeather6'][0]['status'] == "ok":
                for item in weatherJSON['HeWeather6'][0]['air_now_station']:
                    if item['asid'] == 'CNA1007':
                        if int(item['aqi']) is not 0:
                            return int(item['aqi'])
                if weatherJSON['HeWeather6'][0].has_key('air_now_city'):
                    return int(weatherJSON['HeWeather6'][0]['air_now_city']['aqi'])
                else:
                    return -1
            else:
                return -1
        except:
            return -1

if __name__ == "__main__":
    while True:
        pm25 = get_pm25()
        if pm25 == -1:
            time.sleep(30)
            continue

        SAKS.ledrow.on()
        if pm25 < 15:
            SAKS.ledrow.off_for_index(0)
        if pm25 < 35:
            SAKS.ledrow.off_for_index(1)
        if pm25 < 75:
            SAKS.ledrow.off_for_index(2)
        if pm25 < 115:
            SAKS.ledrow.off_for_index(3)
        if pm25 < 150:
            SAKS.ledrow.off_for_index(4)
        if pm25 < 200:
            SAKS.ledrow.off_for_index(5)
        if pm25 < 250:
            SAKS.ledrow.off_for_index(6)
        if pm25 < 300:
            SAKS.ledrow.off_for_index(7)

        SAKS.digital_display.show(("%4d" % pm25).replace(' ','#'))
        time.sleep(1800)
