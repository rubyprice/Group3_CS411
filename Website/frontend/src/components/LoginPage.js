import React, { Component } from 'react'
import ReactDOM from 'react-dom';
import { GoogleLogin } from 'react-google-login';
import axios from "axios";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

const configFile = require('./../configsrc.json')

export default class LoginPage extends Component {
    constructor(props){
    super(props);
    this.state = {
      userData: {},
    };
  }

    showHidden = () => {
        document.getElementById("initialHidden").style.visibility = 'visible';
    }

    onSuccess = (res) => {
        console.log('[Login Success] currentUser:', res.profileObj);
        this.state.userData = res.profileObj;
        console.log(this.state.userData);
        axios.post('http://127.0.0.1:8000/api/GoogleUserData/', this.state.userData)
        .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });

          window.location.replace("http://127.0.0.1:3000/DataEntry");

    }

    onFailrue = (res) => {
        console.log('[Login Failed] res:', res);
    }

    
    render() {
        return (
            <div className="container">
                <form>
                <h3>Sign In with Google</h3>
                
                <div className="form-group">
                    <GoogleLogin
                        clientId={configFile.googleClientId}
                        buttonText="Log in with Google"
                        onSuccess={this.onSuccess}
                        onFailure={this.onFailrue}
                        cookiePolicy={'single_host_origin'}
                    />
                </div>
          
                <div id="initialHide">
                    <button style={{display: 'none'}} type="submit" className="btn btn-primary btn-block">Continue</button>
                </div>
            </form>
        </div>
        )
  }
}
