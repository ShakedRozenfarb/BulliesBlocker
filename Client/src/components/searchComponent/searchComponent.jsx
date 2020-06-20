import React, { Component } from "react";
import classNames from "classnames";
import './searchComponent.less';
import regeneratorRuntime from "regenerator-runtime";
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";
import Loader from 'react-loader-spinner'
import OutsideAlerter from "../outsideAlerterComponent/outsideAlerterComponent.jsx";
import ServerRequestsService from "../../services/serverRequestsService.jsx";

class Search extends Component {
    constructor(props){
        super(props);
        this.serverService = new ServerRequestsService();
        this.state = {
            value: '',
            loading: false,
            suggestions: []
        };

        this.handleClickOutside = this.handleClickOutside.bind(this);
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

    async typeText(event) {
        if(!this.state.value){
            this.setState({suggestions: []});
            return;
        }

        this.serverService.searchUsers(this.state.value).then(response => {
            const suggestions = response.map((user)=>{
                return {
                    label: user.screen_name
                }
            });
            this.setState({suggestions: suggestions});
        });

    }

    debounceSearch = _.debounce((event) => {
        this.typeText(event);
    }, 300);

    search = (event) => {
        if (event.key === 'Enter') {
            this.typeText(event);
        } else {
            this.debounceSearch(event);
        }
    };

    chooseSuggestion(userHandle) {
        this.setState({value: userHandle, suggestions: []});
    }

    getDropDown() {
        const dropDownList = this.state.suggestions.map((suggestion, index)=>
            <div key = {index} className="suggestion dropdown-item" onClick={() =>this.chooseSuggestion(suggestion.label)}>
                {suggestion.label}
            </div>
        );
        return dropDownList;
    }

    handleClickOutside() {
        this.setState({suggestions: []});
    }

    render() {
        return (
            <div className="center">
                <h1 className="app-title">Bully Blocker</h1>
                <textarea value={this.state.value} onChange={this.handleChange} onKeyUp={($event) => this.search($event)} placeholder="Please enter twitter handle"/>
                <input className="searchButton" type="submit" value="Submit" onClick={event =>this.handleSubmit(event)}/>
                <OutsideAlerter handleClick={this.handleClickOutside}>
                    <div className={classNames('dropdown', { hide: !this.state.suggestions.length})}>
                        {
                            this.getDropDown()
                        }
                    </div>
                </OutsideAlerter>
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
