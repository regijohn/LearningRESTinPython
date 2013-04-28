import urllib2
import json

js = json.dumps({'data1':1, 'data2':2})
headers = {'Content-Type':'application/json; charset=utf-8'}
req = urllib2.Request('http://192.168.1.5:8080/perfdata', js, headers)

resp = urllib2.urlopen(req)

print resp.read()
