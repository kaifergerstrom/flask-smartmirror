/**
 * Abstract Class Widget.
 *
 * @class Widget
 */
export class Widget {

    constructor() {
        if (this.constructor == Widget) {
            throw new Error("Abstract classes can't be instantiated.");
        }
    }

    // Only function to modify for each widget
    __build() {
        return "";
    }

    open(json) {
        this.json = json;
        var html = this.__build();
        $("#widget-content").fadeOut('slow', function() {
            $("#widget-content").html(html);
            $("#widget-content").fadeIn();
        });
    }
    
}