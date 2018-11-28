import requests
import json
from urllib.request import urlopen

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

def get_geo():
	# Grab location information from IP through web scraping
	IP = requests.get('http://ip.42.pl/raw').text
	print(IP)
	url = 'https://ipapi.co/{}/json/'.format(IP)
	response = urlopen(url)
	data = json.load(response)

	IP = data['ip']
	org = data['org']
	city = data['city']
	country = data['country']
	latitude = data['latitude']
	longitude = data['longitude']
	region = data['region']

	return latitude, longitude


def get_weather():

	APIKEY = '6b4e2599041ea02b9f19e4e86ae23f59'
	LAT, LON = get_geo()
	URL = 'https://api.darksky.net/forecast/{}/{},{}'.format(APIKEY, LAT, LON)
	print(URL)
	r = requests.get(URL)
	json = r.json()
	currently = json['currently']
	hourly = json['hourly']

	title = currently['summary']
	icon = icon_lookup[currently['icon']]
	temperature = int(round(currently['temperature']))
	desc = hourly['summary'].rstrip('.')

	return {'title':title, 'icon':icon, 'temperature':temperature, 'desc':desc}


if __name__ == "__main__":
	get_weather()
