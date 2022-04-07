import React, { Component } from "react";
import ZipcodeForm from "./components/ZipcodeForm";
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

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("api/UserData/")
      .then((res) => this.setState({ weatherData: res.data }))
      .catch((err) => console.log(err));
      console.log(this.state);
  };

 
  renderItems = () => {
    const newItems = this.state.weatherData;
    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span

          className={`userDataList-userName mr-2`}
          title={item.userName}
        >
          {item.userName}<br />
          {item.zipcode} <br />
          {item.weather} <br />
          {item.date} <br />

        </span>

      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-black text-center my-4">Weather-Recs App</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-1">
              <div className="mb-4">
              </div>
              <ZipcodeForm/>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
      </main>
    );
  }
}



export default App;
