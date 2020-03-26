	
// Small function to convert military time to 12 hour time
function hours12(date) {return (date.getHours() + 24) % 12 || 12;}

function update_time() {

	var d = new Date();  // Javascript date object to fetch updated date

	var hour = hours12(d);  // Returns normal 12 hour hour (not military)
	var minute = d.getMinutes();  // minute count
	var day = d.getDate();  // Get full month day number

	// Convert day and month int to string representation
	var day_name = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"][d.getDay()];
	var month_name = ["January", "February", "March", "April", "May", "June",
	"July", "August", "September", "October", "November", "December"][d.getMonth()];
	
	// Set the updated time to the clock
	$('#time-top').text("0" + hour + ":" + minute);
	$('#time-mid').text(day_name);
	$('#time-bottom').text(month_name + ' ' + day);	

}

function update_weather() {

	// Send an ajax post request to get updated weather from flask
	req = $.ajax({
		url : '/update_weather',
		type : 'POST',
		data : {}
	});

	req.done(function(data) {

		// Split the data from the updated weather json
		var desc = data.currentWeather.desc;
		var icon = data.currentWeather.icon;
		var temperature = data.currentWeather.temperature;
		var title = data.currentWeather.title;
		
		// Update the html elements with the data
		$('.weather-current-temp').text(temperature + String.fromCharCode(176));
		$('#weather-current-img').attr('src', '/static/' + icon);
		$('.weather-current-title').text(title);
		$('.weather-current-desc').text(desc);

	});

}

update_weather();  // Update the weather on the boot up

setInterval(update_time, 1000);  // Update the time every second
setInterval(update_weather, 600000);  // Update the time every 10 minutes
