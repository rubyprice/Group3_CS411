import React, { Component } from 'react'
import axios from "axios";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


export default class MovieScrollableList extends Component {
    constructor(props) {
        super(props);
        this.state = {
          movieData: [],
        };
      }

    componentDidMount() {
        this.refreshList2();
    }

    refreshList2 = () => {
        axios
        .get("http://localhost:8000/api/IMDBMovies/")
        .then((res) => this.setState({ movieData: res.data }))
        .catch((err) => console.log(err));
    };

    fillScrollableList = () => {
        const newItems = this.state.movieData;
        // console.log(this.state);
        return newItems.map((item) => (
        <div>
            <span>
                <img src={item.image} alt="IMG NOT FOUND" width={120} length={120}/>
                <p style={{ fontSize: '55px'}}> <strong>{item.title}</strong>({item.description})</p>
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
