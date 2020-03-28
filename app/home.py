from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, send

from scripts.weather import get_weather
from scripts.CommandHandler import CommandHandler
#from scripts.widgets.NewsWidget import get_news

from scripts.agent.classes.Listener import Listener

import datetime, requests, time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

thread = None  # Thread variable for listener

listener = Listener()
listener.run()

command_handler = CommandHandler()


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
	prev_command = None                                               
	while True:
		curr_command = listener.get_command()
		print(curr_command)
		if (curr_command != prev_command and curr_command != ""):
			#print(curr_command)
			request = command_handler.run(curr_command)
			print(request)
			socketio.emit('command', request);
			try:
				command_handler.speak()
			except:
				pass

		prev_command = curr_command
		'''
		if not (i % 2 == 0):                                        
			socketio.emit('command', {'open': "news", 'data':get_news()});
			print("running news");
		else:
			socketio.emit('command', {'close': "none"})
		time.sleep(10)
		i += 1
		'''


@socketio.on('connect')                                                         
def connect():                                                                  
	global thread                                                               
	if thread is None:                                                          
		thread = socketio.start_background_task(target=background_thread)   


if __name__ == '__main__':
	socketio.run(app)