
import requests

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

	APIKEY = '6b4e2599041ea02b9f19e4e86ae23f59'
	LAT = 37.8267
	LON = -122.4233
	URL = 'https://api.darksky.net/forecast/{}/{},{}'.format(APIKEY, LAT, LON)

	r = requests.get(URL)
	json = r.json()
	currently = json['currently']

	title = currently['summary']
	icon = icon_lookup[currently['icon']]
	temperature = int(round(currently['temperature']))

	return {'title':title, 'icon':icon, 'temperature':temperature}


'''
url = 'http://ipinfo.io/json'
response = requests.get(url)
data = response.json()
'''