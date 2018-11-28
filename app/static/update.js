setInterval(function() {

	console.log($('#time-top').text())

	var time_top = $('#time-top').text()
	var time_mid = $('#time-mid').text()
	var time_bottom = $('#time-bottom').text()

	req = $.ajax({
		url : '/update',
		type : 'POST',
		data : { time_top : time_top, time_mid : time_mid, time_bottom : time_bottom}
	});

	req.done(function(data) {

		// Updated data for time
		var day = data.currentTime.day
		var day_num = data.currentTime.day_num
		var hour = data.currentTime.hour
		var minute = data.currentTime.minute
		var month = data.currentTime.month

		$('#time-top').text(hour + ':' + minute);
		$('#time-mid').text(day);
		$('#time-bottom').text(month + ' ' + day_num);

		var desc = data.currentWeather.desc
		var icon = data.currentWeather.icon
		var temperature = data.currentWeather.temperature
		var title = data.currentWeather.title
		console.log(icon)
		$('.weather-current-temp').text(temperature + String.fromCharCode(176))
		$('#weather-current-img').attr('src', '/static/' + icon);
		$('.weather-current-title').text(title)
		$('.weather-current-desc').text(desc)
		

	});

	console.log(req)

}, 30000);