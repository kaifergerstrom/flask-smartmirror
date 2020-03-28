from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, send

from widgets.Weather import get_weather
from widgets.News import get_news

import datetime, requests, time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

thread = None

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


@app.route("/update_widget", methods=['POST'])
def update_widget():
	'''
	Returns the widget data from the assistant
	'''
	json = get_news()
	return jsonify({'result' : 'success', 'json' : json, 'widget' : 'news'})
	

def background_thread():     
	i = 0                                                   
	while True:
		if (i % 2 == 0):                                        
			socketio.emit('command', {'open': "news"})
		else:
			socketio.emit('command', {'open': "music"})
		time.sleep(10)
		i += 1


@socketio.on('connect')                                                         
def connect():                                                                  
	global thread                                                               
	if thread is None:                                                          
		thread = socketio.start_background_task(target=background_thread)   


if __name__ == '__main__':
	socketio.run(app)