/**
 * Class CommandRunner.
 *
 * @class CommandRunner
 */
export default class CommandRunner {

    constructor() {
        this.commands = {"open" : {}, "close": "closing"};
    }

    add_command(key, widget) {
        this.commands["open"][key] = widget;
    }

    run_command(json) {
        var key = Object.keys(json)[0];
        console.log(key);
        if (key == "open") {
            this.commands["open"][json[key]].open(json);
        } else if (key == "close") {
            this.clear_window();
        }
    }

    clear_window() {
        $("#widget-content").fadeOut('slow', function() {
            $("#widget-content").html("");
        });
    }

}

