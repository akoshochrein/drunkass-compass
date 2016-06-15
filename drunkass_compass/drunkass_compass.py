
import googlemaps
import keyring
import json
import requests
from datetime import datetime
import commands
from bs4 import BeautifulSoup


def main():
    # get API key for google maps
    api_key = keyring.get_password('drunkass-compass-api-key', 'drunkass-compass-api-key')
    if api_key is None:
        print 'Missing google maps api key'
        exit(1)

    # get current location
    (status, output) = commands.getstatusoutput("CoreLocationCLI -once YES -format '%latitude %longitude'")
    if status != 0:
        print "Could not run CoreLocationCLI, using freegeoip - this is not accurate"    
        response_json = json.loads(requests.get('http://freegeoip.net/json/').content)
        lat = response_json['latitude']
        lng = response_json['longitude']
    else:
        (lat, lng) = output.split()

    # get the nearest pubs
    gmaps = googlemaps.Client(key=api_key)
    places = gmaps.places('pub|bar',
        location={'lat': lat, 'lng': lng},
        radius=100
    )

    for place in places['results']:
        directions_result = gmaps.directions({'lat': lat, 'lng': lng},
                                     place['geometry']['location'],
                                     mode='walking')
                     
        print "{name} ({address})".format(name=place['name'].encode('utf8'), address=place['formatted_address'].encode('utf8'))
        for step in directions_result[0]['legs'][0]['steps']:
            print "\t", BeautifulSoup(step['html_instructions'], 'html.parser').get_text()


if __name__ == '__main__':
    main()
