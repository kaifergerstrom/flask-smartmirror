
import {Widget} from "../classes/Widget.js"
/**
 * NewsWidget, get updated news and display them
 *
 * @class NewsWidget
 * @extends {Widget}
 */
export default class NewsWidget extends Widget {

    __build() {
         
        var headlines = "";

        for (var headline in this.json['data']) {

            var headline_html = `
            <div class='headline-container'>
                <div class='headline-icon'><img src='/static/assets/News.png'></div>
                <div class='headline-text'>${headline}</div>
            </div>
            `
            headlines = headlines.concat(headline_html)
            
        }

        var html = `
        <div class='app-main-container'>
            <div class='news-app-container'>
                ${headlines}
            </div>
        </div>
        `;

        console.log("Opening news app!");

        return html;
    }

}