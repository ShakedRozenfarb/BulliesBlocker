import React, { Component } from "react";
import './searchComponent.less';
import regeneratorRuntime from "regenerator-runtime";
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";
import Loader from 'react-loader-spinner'

class Search extends Component {
    constructor(props){
        super(props);
        this.state = {
            value: '',
            loading: false
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    async handleSubmit() {
        this.setState({loading: true});
        await this.props.getUserResults(this.state.value);
    }

    render() {
        return (
            <div className="center">
                <h1 className="app-title">Bully Blocker</h1>
                <textarea value={this.state.value} onChange={this.handleChange} placeholder="Please enter twitter handle"></textarea>
                <input className="searchButton" type="submit" value="Submit" onClick={event =>this.handleSubmit(event)}/>
                {this.state.loading ?
                    <div style={{marginLeft: '43%'}}>
                    <Loader
                    type="ThreeDots"
                    color="#40b6ce"
                    height={100}
                    width={100}
                /> </div>: null }
            </div>
        )
    }
}

export default Search;
