from flask import Flask, render_template, jsonify
from widgets.Weather import get_weather
from widgets.Time import get_time
from widgets.News import get_news

import datetime
import requests

currentTime = get_time()
currentWeather = get_weather()
currentNews = get_news()
print(currentNews)

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home():
	return render_template('home.html', currentTime=currentTime, currentWeather=currentWeather, currentNews=currentNews)

@app.route("/update", methods=['POST'])
def update():

	currentTime = get_time()
	currentWeather = get_weather()

	time_top = '{}:{}'.format(currentTime['hour'], currentTime['minute'])
	time_mid = currentTime['day']
	time_bottom = '{} {}'.format(currentTime['month'], currentTime['day_num'])

	return jsonify({'result' : 'success', 'currentTime' : currentTime, 'currentWeather' : currentWeather})

if __name__ == '__main__':
	app.run(debug=True)