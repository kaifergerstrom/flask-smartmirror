from flask import Flask, render_template
from Weather import get_weather
from Time import get_time
import datetime
import requests

currentTime = get_time()
currentWeather = get_weather()

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def hello():
	return render_template('home.html', currentTime=currentTime, currentWeather=currentWeather)

if __name__ == '__main__':
	app.run(debug=True)