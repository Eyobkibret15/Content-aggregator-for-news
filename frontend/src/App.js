import React from "react";
import './App.css';

import Navbar from './components/Navbar/Navbar'

let allNews= {};
class App extends React.Component {

  componentDidMount(){
   fetch('http://127.0.0.1:5000/')
  .then(response => response.json())
  .then(json => {
      allNews = json
      console.log(allNews)})
  }

  render(){
  return (
    <div className="App">
      <Navbar />
    </div>
  );
}
}

export default App;
