import React, { Component } from "react";
import { useHistory } from "react-router-dom";
import { Button } from 'react-bootstrap';
import DataEntry from "./components/DataEntry";
import ZipcodeForm from "./components/ZipcodeForm";
import LoginPage from "./components/LoginPage";
import axios from "axios";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      weatherData: [],
    };
  }

 

  render() {
    if (window.location.href == "http://127.0.0.1:3000/" || window.location.href == "http://localhost:3000/"){
      return (
        <div id="page1">
          <LoginPage/>
        </div>
      );
    }
    else if (window.location.href == "http://127.0.0.1:3000/DataEntry" || window.location.href == "http://localhost:3000/DataEntry"){
      return (
        <div id="page2">
          <DataEntry/>
        </div>
      )
    }
  }
}



export default App;