import React, { Component } from 'react';
import { Form, Button } from 'react-bootstrap';

export default class ZipcodeForm extends Component {
  constructor(props){
    super(props);
  }


  render() {
    return (

    <div className='container'>
      <Form action="http://127.0.0.1:8000/api/UserData/" method="POST">
        <Form.Group>
          <Form.Label>Username</Form.Label>
          <Form.Control type="text" name="userName" required/>

          <Form.Label>Zipcode</Form.Label>
          <Form.Control type="text" name="zipcode" required/>
        </Form.Group>


        <Form.Group>
          <Button variant="primary" type="submit">
            Submit
          </Button>
        </Form.Group>

      </Form>
      </div>

    )
  }
}
