from flask import Flask, render_template
#from time import get_time
import datetime


def get_time():
	currentTime = datetime.datetime.now()
	hour = currentTime.hour
	minute = currentTime.minute
	day = currentTime.strftime("%A")
	month = currentTime.strftime("%B")
	day_num = currentTime.day

	return {'hour': hour, 'minute': minute, 'day': day, 'month': month, 'day_num': day_num}

currentTime = get_time()

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def hello():
	return render_template('home.html', currentTime=currentTime)

if __name__ == '__main__':
	app.run(debug=True)