import React, { Component } from "react";
import ReactDOM from "react-dom";
import Search from "../searchComponent/searchComponent.jsx";

import './mainComponent.less';

class Main extends Component {
    render() {
        return (
        <div>
            <a>app logo</a>
            <Search/>
        </div>
        )
    }
}

export default Main;
const wrapper = document.getElementById("container");
wrapper ? ReactDOM.render(<Main />, wrapper) : false;