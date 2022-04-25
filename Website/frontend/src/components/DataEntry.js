import React, { Component } from 'react'
import axios from "axios";
import ZipcodeForm from "./ZipcodeForm";
import ScrollableList from "./ScrollableList";
import MovieScrollableList from "./MovieScrollableList";
import { Button } from 'react-bootstrap';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export default class DataEntry extends Component {
    constructor(props) {
        super(props);
        this.state = {
          weatherData: [],
        };
      }
    
      
      componentDidMount() {
        this.refreshList();
      }
    
      refreshList = () => {
        axios
          .get("api/UserData/")
          .then((res) => this.setState({ weatherData: res.data }))
          .catch((err) => console.log(err));
      };


      renderItems = () => {
        const newItems = this.state.weatherData;
        // console.log(this.state);
        return newItems.map((item) => (
          <li
            key={item.id}
            className="list-group-item d-flex justify-content-between align-items-center"
          >
            <span
    
              className={`userDataList-userName mr-2`}
              title={item.givenName}
            >
              {item.givenName}<br />
              {item.zipcode} <br />
              {item.weather} <br />
              {item.date} <br />
    
            </span>
    
          </li>
        ));
      };
    
    
      render() {
            return (
        <div id="page1">
        <main className="container">
            <h1 className="text-black text-center my-4">Show Spotify Playlists and Movie Reccomendations To Match the Weather!</h1>
            <div className="row">
            <div className="col-md-6 col-sm-10 mx-auto p-0">
                <div className="card p-1">
                <div className="mb-4">
                </div>
                <ZipcodeForm/>
                <p><ScrollableList/>
                <MovieScrollableList/></p> 
                <ul className="list-group list-group-flush border-top-0">
                    
                </ul>
                {/* <Button color="primary" className="px-4" onClick={this.routeChange}>Next Page</Button>                 */}
                </div>
            </div>
            </div>
        </main>
        </div>
        );
    }
      
}
