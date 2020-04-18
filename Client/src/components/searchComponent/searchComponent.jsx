import React, { Component } from "react";
import ReactDOM from "react-dom";

import './searchComponent.less';

class Search extends Component {
    constructor(props){
        super(props);
        this.state = {
            value: ''
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        //TODO: make http request to server
        event.preventDefault();
    }

    render() {
        return (
            <div>
                <textarea value={this.state.value} onChange={this.handleChange} placeholder="type twitter user id"></textarea>
                <input className="searchButton" type="submit" value="Submit" />
            </div>
        )
    }
}

export default Search;