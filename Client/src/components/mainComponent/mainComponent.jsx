import React, { Component } from "react";
import ReactDOM from "react-dom";
import Search from "../searchComponent/searchComponent.jsx";

import './mainComponent.less';
import ServerRequestsService from "../../services/serverRequestsService.jsx";
import ResultsComponent from "../resultsComponent/resultsComponent.jsx";

class Main extends Component {

    constructor(props) {
        super(props);
        this.serverService = new ServerRequestsService();
        this.state = {
            userResults: null,
            userName: ''
        };

        this.getUserResults = this.getUserResults.bind(this);
    }

    async getUserResults(userName) {
        const userResults = await this.serverService.getUserResults(userName);
        this.setState({userResults: userResults, userName: userName});
    }

    render() {
        return (
        <div>
            {this.state.userResults ? <ResultsComponent userName={this.state.userName} userResults={this.state.userResults} /> : <Search getUserResults={this.getUserResults} /> }
        </div>
        )
    }
}

export default Main;
const wrapper = document.getElementById("container");
wrapper ? ReactDOM.render(<Main />, wrapper) : false;
