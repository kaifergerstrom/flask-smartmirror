
import {Widget} from "../Widget.js"
/**
 * NewsWidget.
 *
 * @class NewsWidget
 * @extends {Widget}
 */
export default class MusicWidget extends Widget {

    __build() {
        console.log(this.json)
        return "<b>Music Time</b>";
    }

}