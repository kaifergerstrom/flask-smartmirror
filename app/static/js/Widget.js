/**
 * Abstract Class Widget.
 *
 * @class Widget
 */
class Widget {

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

/**
 * NewsWidget.
 *
 * @class NewsWidget
 * @extends {Widget}
 */
class NewsWidget extends Widget {

    __build() {
        console.log(this.json)
        return "<b>Test</b>";
    }

}

new NewsWidget().open();

//close_widget(html);