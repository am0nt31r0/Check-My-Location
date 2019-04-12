#!/usr/bin/python3

import urllib.request
import urllib.error
import json

try:
    urllib.request.urlopen("https://ipecho.net/plain", timeout = 1)

except urllib.error.URLError as e:

    print ('Network connection is down...')

else:
    
    key="" # insert your API key here
    pub_ip = urllib.request.urlopen("http://ipecho.net/plain").read().decode('utf-8')
    data = urllib.request.urlopen("http://api.ipstack.com/" + str(pub_ip) + "?access_key=" + key).read().decode('utf-8')

    j = json.loads(data)
    print ("[*] IP: " + j['ip'])
    print ("[*] CONTINENT: " + j['continent_name'])
    print ("[*] COUNTRY/CITY: " + j['country_name'] + " - " + j['city'] + " (" + j['zip'] + ")")
    print ("[*] LATITUDE: " + str(j['latitude']) + " LONGITUDE: " + str(j['longitude']))
