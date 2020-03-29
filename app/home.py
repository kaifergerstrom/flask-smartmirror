from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, send

from scripts.weather import get_weather
from scripts.CommandHandler import CommandHandler
#from scripts.widgets.NewsWidget import get_news

from scripts.agent.classes.Listener import Listener

import datetime, requests, time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

socketio = SocketIO(app)  # Initialize socket api

thread = None  # Thread variable for listener

# Run the voice recording listener
listener = Listener(name="mirror mirror")
listener.run()

command_handler = CommandHandler()  # Create command handler object for listener


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
	
# Listen for changes to the command
def command_listener(): 

	prev_command = None      

	while True:

		curr_command = listener.get_command()  # Get the full phrase from the listener
		print(curr_command)

		if (curr_command != prev_command and curr_command != ""):  # Detect changes in the command
			
			request = command_handler.run(curr_command)
			socketio.emit('command', request);

			try:
				command_handler.speak()  # If the command has a script attached, speak...
			except:
				pass

		prev_command = curr_command  # 


@socketio.on('connect')                                                         
def connect():                                                                  
	global thread  # Fetch the thread variable to only create one thread                                                              
	if thread is None:                                                          
		thread = socketio.start_background_task(target=command_listener)  # Run listener in background socket function


if __name__ == '__main__':
	socketio.run(app)