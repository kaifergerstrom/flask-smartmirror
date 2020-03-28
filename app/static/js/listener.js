
import NewsWidget from "./widgets/NewsWidget.js";
import MusicWidget from "./widgets/MusicWidget.js";

var commands = {
 "news" : new NewsWidget(),
 "music" : new MusicWidget(),
};


$(document).ready(function() {

    var socket = io.connect('http://127.0.0.1:5000');

    socket.on('connect', function() {
         console.log('connected');
    });
    
    socket.on('command', function(data) {
        console.log(data);
        commands[data["open"]].open();
    });

});