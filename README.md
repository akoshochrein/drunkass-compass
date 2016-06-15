# Drunkass Compass
A compass for the desperate, when they just cannot get away from the terminal to grab a drink.

## Usage

### Regular
```$ drunkass-compass```

### Roulette
```$ drunkass-compass | shuf | head -1```

## Installation
Get a Google Maps API key [here](https://console.developers.google.com/flows/enableapi?apiid=maps_backend,geocoding_backend,directions_backend,distance_matrix_backend,elevation_backend&keyType=CLIENT_SIDE&reusekey=true&pli=1)  
Enable the places API for that project [here](https://console.developers.google.com/apis/api/places_backend?project=_)  
Add your Google Maps API key to your compass as such:
```
$ python -c 'import keyring; keyring.set_password("drunkass-compass-api-key", "drunkass-compass-api-key", "MY_API_KEY")'
```
Install the application:
```
$ pip install drunkass-compass
```
