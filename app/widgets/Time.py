import datetime

def get_time():
	currentTime = datetime.datetime.now()
	hour = currentTime.strftime("%I")
	minute = currentTime.strftime("%M")
	day = currentTime.strftime("%A")
	month = currentTime.strftime("%B")
	day_num = currentTime.day
	return {'hour': hour, 'minute': minute, 'day': day, 'month': month, 'day_num': day_num}


if __name__ == "__main__":
	get_time()
