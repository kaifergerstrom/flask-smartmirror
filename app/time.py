import datetime

def get_time():
	currentTime = datetime.datetime.now()
	hour = currentTime.hour
	minute = currentTime.minute
	day = currentTime.strftime("%A")
	month = currentTime.strftime("%B")
	day_num = currentTime.day

	return {'hour': hour, 'minute': minute, 'day': day, 'month': month, 'day_num': day_num}