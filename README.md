# Drunkass Compass
A compass for the desperate, when they just cannot get away from the terminal to grab a drink.

## Usage

### Regular
```$ drunkass-compass```

### Roulette
```$ drunkass-compass | shuf | head -1```

## Installation
Add your Google Maps API key to your compass as such:
```
$ python -c 'import keyring; keyring.set_password("drunkass-compass-api-key", "drunkass-compass-api-key", "MY_API_KEY")'
```
Install the application:
```
$ pip install drunkass-compass
```
