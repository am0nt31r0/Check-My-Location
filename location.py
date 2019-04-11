#!/usr/bin/python3

from urllib.request import urlopen
import json

key=""
pub_ip = urlopen("http://ipecho.net/plain").read().decode('utf-8')
data = urlopen("http://api.ipstack.com/" + str(pub_ip) + "?access_key=" + key).read().decode('utf-8')

j = json.loads(data) 
print ("IP: " + j['ip'])
print ("CONTINENT: " + j['continent_name'])
print ("COUNTRY/CITY: " + j['country_name'] + " - " + j['city'] + " (" + j['zip'] + ")")
print ("LATITUDE: " + str(j['latitude']) + " LONGITUDE: " + str(j['longitude']))
