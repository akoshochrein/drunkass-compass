
import googlemaps
import keyring
import json
import requests


# get API key for google maps
api_key = keyring.get_password('drunkass-compass-api-key', 'drunkass-compass-api-key')
if api_key is None:
    print 'Missing google maps api key'
    exit(1)

# get current location
response_json = json.loads(requests.get('http://freegeoip.net/json/').content)
lat = response_json['latitude']
lng = response_json['longitude']

# get the nearest pubs
gmaps = googlemaps.Client(key=api_key)
places = gmaps.places('pub|bar',
    location={'lat': lat, 'lng': lng},
    radius=100
)

for place in places['results']:
    print place['name']
