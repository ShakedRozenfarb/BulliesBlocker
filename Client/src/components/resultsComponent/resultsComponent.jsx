import React, { Component } from "react";
import ReactDOM from "react-dom";

import './resultsComponent.less';

class ResultsComponent extends Component {

    constructor(props) {
        super(props);
        this.state = {
            userResults: this.props.userResults
        }
    }

    render() {
        return (
            <div>
                {`${this.state.userResults.user} has a bullying score of ${this.state.userResults.score}`}
                <div className="box">
                {this.state.userResults.userTweets.map(tweet =>
                    <div>
                        <div>{tweet.text}</div>
                        <div>{tweet.bullying}</div>
                    </div>
                )}
                </div>
            </div>
        )
    }
}

export default ResultsComponent;

