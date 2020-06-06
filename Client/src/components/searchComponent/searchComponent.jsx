import React, { Component } from "react";
import './searchComponent.less';
import regeneratorRuntime from "regenerator-runtime";

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

    async handleSubmit() {
        await this.props.getUserResults();
    }

    render() {
        return (
            <div className="center">
                <h1 className="app-title">Bully Blocker</h1>
                <textarea value={this.state.value} onChange={this.handleChange} placeholder="type twitter user id"></textarea>
                <input className="searchButton" type="submit" value="Submit" onClick={event =>this.handleSubmit(event)}/>
            </div>
        )
    }
}

export default Search;
