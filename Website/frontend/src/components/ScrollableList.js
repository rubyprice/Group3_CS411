import React, { Component } from 'react'
import axios from "axios";
import ReactScrollableList from "react-scrollable-list";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


export default class ScrollableList extends Component {
    constructor(props) {
        super(props);
        this.state = {
          spotifyData: [],
        };
      }

    componentDidMount() {
        this.refreshList2();
    }

    refreshList2 = () => {
        axios
        .get("http://localhost:8000/api/SpotifyPlaylists/")
        .then((res) => this.setState({ spotifyData: res.data }))
        .catch((err) => console.log(err));
    };

    fillScrollableList = () => {
        const newItems = this.state.spotifyData;
        // console.log(this.state);
        return newItems.map((item) => (
        <div>
            <span>
                <img src={item.playlist_img} alt="IMG NOT FOUND" width={120} length={120}/>
                <a style={{ fontSize: '70px'}} href={item.external_url_spotify}>{item.playlist_name}</a>
            </span>
            <hr />
        </div>
        
        ));
      };
    

  render() {
    return (
      <div className='scroll'>
        {this.fillScrollableList()}
      </div>
    )
  }
}
