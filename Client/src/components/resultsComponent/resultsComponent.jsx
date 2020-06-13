import React, { Component } from "react";
import ReactDOM from "react-dom";

import './resultsComponent.less';

class ResultsComponent extends Component {

    constructor(props) {
        super(props);
        this.state = {
            userResults: this.props.userResults,
            userName: this.props.userName
        }
    }

    render() {
        return (
            <div>
                <div className="left">
                <div className="results-title">{`${this.state.userName} Bullying Results`}</div>
                <div className="score-results">{`${this.state.userName} has a bullying score of ${this.state.userResults.score * 100}`}</div>
                </div>
                <div className="tweets">
                <div className="box-title">{`${this.state.userName} Latest Tweets`}</div>
                <div className="box">
                {this.state.userResults.tweets.map(tweet =>
                    <div className="list-item" key={tweet.tweet_id}>
                        <div className="tweet-message">{tweet.tweet_message}</div>
                        <div className="tweet-classification">{tweet.is_bully.toString()}</div>
                    </div>
                )}
                </div>
                </div>
            </div>
        )
    }
}

export default ResultsComponent;

