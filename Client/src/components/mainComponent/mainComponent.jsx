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
            userResults: null
        }
    }

    async getUserResults() {
        const userResults = await this.serverService.getUserResults(this.state.value);
        this.setState({userResults: userResults});
    }

    render() {
        return (
        <div>
            {this.state.userResults ? <ResultsComponent userResults={this.state.userResults} /> : <Search getUserResults={this.getUserResults} /> }
        </div>
        )
    }
}

export default Main;
const wrapper = document.getElementById("container");
wrapper ? ReactDOM.render(<Main />, wrapper) : false;
