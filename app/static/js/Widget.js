/**
 * Abstract Class Widget.
 *
 * @class Widget
 */
export class Widget {

    constructor(json) {
        if (this.constructor == Widget) {
            throw new Error("Abstract classes can't be instantiated.");
        }
        this.json = json;
        this.html = this.__build();
    }

    // Only function to modify for each widget
    __build() {
        return "";
    }

    open() {
        this.close();
        $("#widget-content").html(this.html);
        console.log(this.html);
        $("#widget-content").fadeIn();
        console.log("Opened widget");
    }

    close() {
        // Fade out and remove widget information
        $("#widget-content").fadeOut();
        $("#widget-content").html("");
        console.log("Closed widget");
    }

}