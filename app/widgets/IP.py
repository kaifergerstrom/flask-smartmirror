import json
from urllib.request import urlopen

def fetch_ip():
	# Grab location information from IP through web scraping
	url = 'https://ipapi.co/8.8.8.8/json/'
	response = urlopen(url)
	data = json.load(response)

	IP = data['ip']
	org = data['org']
	city = data['city']
	country = data['country']
	latitude = data['latitude']
	longitude = data['latitude']
	region = data['region']

	return latitude, longitude