import requests
import json

# Icon dictionary for relative images
icon_lookup = {
	'clear-day': "assets/Sun.png",  # clear sky day
	'wind': "assets/Wind.png",   #wind
	'cloudy': "assets/Cloud.png",  # cloudy day
	'partly-cloudy-day': "assets/PartlySunny.png",  # partly cloudy day
	'rain': "assets/Rain.png",  # rain day
	'snow': "assets/Snow.png",  # snow day
	'snow-thin': "assets/Snow.png",  # sleet day
	'fog': "assets/Haze.png",  # fog day
	'clear-night': "assets/Moon.png",  # clear sky night
	'partly-cloudy-night': "assets/PartlyMoon.png",  # scattered clouds night
	'thunderstorm': "assets/Storm.png",  # thunderstorm
	'tornado': "assests/Tornado.png",    # tornado
	'hail': "assests/Hail.png"  # hail
}

def get_weather():

	ip = IP()  # Get current location information

	# Get json from dark skys api
	APIKEY = '6b4e2599041ea02b9f19e4e86ae23f59'
	LAT, LON = ip.latitude, ip.longitude
	URL = 'https://api.darksky.net/forecast/{}/{},{}'.format(APIKEY, LAT, LON)
	r = requests.get(URL)
	json = r.json()

	# Get current and hourly data
	currently = json['currently']
	hourly = json['hourly']
	
	# Fetch important information for display
	title = currently['summary']
	icon = icon_lookup[currently['icon']]
	temperature = int(round(currently['temperature']))
	desc = hourly['summary'].rstrip('.')

	return {'title':title, 'icon':icon, 'temperature':temperature, 'desc':desc}


if __name__ == "__main__":
	from IP import IP
	print(get_weather())
else:
	from widgets.IP import IP
