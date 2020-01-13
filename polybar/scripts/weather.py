#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import urllib
#mport urlparse
#import urllibrequest
import urllib.parse
import urllib.request
import os


def main():
    city = "Kingston, CA"
    api_key = "da1f3c25743ea88ae4cfa4b006e3eee0"

    try:
        data = urllib.parse.urlencode({'q': city, 'appid': api_key, 'units': 'metric'})
        weather = json.loads(urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?' + data)
            .read())
        desc = weather['weather'][0]['description'].capitalize()
        temp_desc = desc

        if weather['weather'][0]['description'].split()[-1].capitalize() == 'Rain':
            temp_desc = 'Rain'
        if weather['weather'][0]['description'].split()[-1].capitalize() == 'Snow':
            temp_desc = 'Snow'
        if weather['weather'][0]['description'].split()[-1].capitalize() == 'Clouds':
            temp_desc = 'Clouds'
        if weather['weather'][0]['description'].split()[-1].capitalize() == 'Drizzle':
            temp_desc = 'Drizzle'

	#desc = desc.split()[-1].capitalize()
        icons = {"Thunderstorm":"", "Drizzle":"", "Rain":"", "Snow":"", "Mist":"", "Haze":"", "Fog":"", "Squall":"", "Clear sky":"","Clouds":""}
        icon = icons.get (temp_desc, 'none')
        temp = int(float(weather['main']['temp']))
        #return icon + ' ' + desc + ' ' + temp + ''
        return '{} {}, {}°C'.format(icon, desc, temp)
        #return '{}°C'.format(temp)
    except:
        return ''
        #return 'Check Connection '


if __name__ == "__main__":
	print(main())

