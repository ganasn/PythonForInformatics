#Chapter 13 - Section 7 - Using Google Maps API

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location>')
    if len(address) < 1:
        break
    
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address':address})
#    print 'Retrieving URL %r', % url
    print url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved %d characters' % len(data)
    
    try: js = json.loads(str(data))
    except: js = None
    
    if 'status' not in js or js['status']  != 'OK':
        print 'Failure to retrieve'
        print data
        continue
        
    print json.dumps(js, indent = 4) #Indent argument formats the json data instead of truly dumping it
#    print 'Now printing json.dumps w/o indent argument'
#    print json.dumps(js)
    
    latitude = js['results'][0]['geometry']['location']['lat']
    longitude = js['results'][0]['geometry']['location']['lng']
    location = js['results'][0]['formatted_address']
    
    print 'latitude: %r\nlongitude: %r\nlocation: %r\n' % (latitude, longitude, location)