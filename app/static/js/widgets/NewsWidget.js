
import {Widget} from "../Widget.js"
/**
 * NewsWidget.
 *
 * @class NewsWidget
 * @extends {Widget}
 */
export default class NewsWidget extends Widget {

    __build() {
        console.log(this.json)
        return "<b>News Time</b>";
    }

}