import React, { Component } from "react";
import './searchComponent.less';
import ServerRequestsService from "../../services/serverRequestsService";

class Search extends Component {
    constructor(props){
        super(props);
        this.serverService = new ServerRequestsService();
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
            <div>
                <textarea value={this.state.value} onChange={this.handleChange} placeholder="type twitter user id"></textarea>
                <input className="searchButton" type="submit" value="Submit" onClick={event =>this.handleSubmit(event)}/>
            </div>
        )
    }
}

export default Search;
