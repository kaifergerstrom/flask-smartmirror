
var html = "<b style='color: red;'>Hello World</b>"

function open_widget(html) {
    $("#widget-content").html(html);
    console.log("Opened widget");
}

function close_widget() {
    $("#widget-content").html("");
    console.log("Cleared widget!");
}

close_widget(html);