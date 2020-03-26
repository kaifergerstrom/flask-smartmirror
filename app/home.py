from flask import Flask, render_template, jsonify

from widgets.Weather import get_weather
from widgets.News import get_news

import datetime, requests

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	'''
	Main directory for smart mirror display
	'''
	return render_template('home.html')


@app.route("/update_weather", methods=['POST'])
def update_weather():
	'''
	Returns updated weather, called every 10 minutes
	'''
	currentWeather = get_weather()
	return jsonify({'result' : 'success', 'currentWeather' : currentWeather})


if __name__ == '__main__':
	app.run(debug=True)