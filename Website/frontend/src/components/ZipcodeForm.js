import React, { Component } from 'react';
import { Form, Button } from 'react-bootstrap';
import axios from "axios";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export default class ZipcodeForm extends Component {
  constructor(props){
    super(props);
    this.state = {
      userData: [],
    };
  }


  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("api/UserData/")
      .then((res) => this.setState({ userData: res.data }))
      .catch((err) => console.log(err));
  };

  renderItems = () => {
    console.log(this.state.userData);
  };

  fillFields = () => {
    console.log('fillFields');
    console.log(this.state.userData[0]);
    document.getElementById("givenName").value = this.state.userData[0].givenName;
    document.getElementById("googleID").value = this.state.userData[0].googleID;
  };

  render() {
    this.renderItems();
    return (
    <div className='container'>
    
      <Form action="http://127.0.0.1:8000/api/UserData/" method="POST">
        <Form.Group>
          <Form.Label  value={this.state.userData.givenName}></Form.Label>
          <Form.Control  style={{display: 'none'}} id='givenName' defaultValue={this.state.userData.givenName} type="text" name="givenName" />

          <Form.Label value={this.state.userData.googleID} ></Form.Label>
          <Form.Control style={{display: 'none'}} id='googleID' defaultValue={this.state.userData.givenName} type="text" name="googleID" />

          <Form.Label value="02215">Zipcode</Form.Label>
          <Form.Control type="text" name="zipcode" required/>

        </Form.Group>


        <Form.Group>
          <Button onClick={this.fillFields} variant="primary" type="submit">
            Show Playlists!
          </Button>
        </Form.Group>

      </Form>
      
      </div>

    )
  }
}
