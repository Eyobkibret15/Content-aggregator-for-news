import React from "react";
import './App.css';

import Navbar from './components/Navbar/Navbar'
import Aljazeera from './components/aljazeera/Aljazeera';
import Bbc from './components/bbc/Bbc';
import FirstNews from './components/firstnews/FirstNews';
import HackerNews from './components/hackernews/HackerNews';
import Tvn24 from './components/tvn24/Tvn24';

import 'tachyons';

// let allNews;


class App extends React.Component {
  
  constructor(){
    super()
    this.state = {
      allNews: {},
      showNews: false
    }
  }

  componentWillMount(){
    fetch('http://127.0.0.1:5000/')
    .then(res => res.json())
    .then(news =>{
       this.setState({allNews: news, showNews: true})
      console.log(this.state.allNews)
      })
  }

  render(){
  return (
    <div className="App">
      <Navbar />
      <div>
        {this.state.showNews ? 
        <div className="newsCompnentsContainer">
          <div><Aljazeera newsList={this.state.allNews.aljazeera} /></div>
          <div><Bbc newsList={this.state.allNews.bbc} /></div>
          <div><FirstNews newsList={this.state.allNews.firstnews} /></div>
          <div><HackerNews newsList={this.state.allNews.hackernews} /></div>
          <div><Tvn24 newsList={this.state.allNews.tvn24} /></div>
        </div>
         : 'Loading ...'}
      </div>      
    </div>
  );
}
}

export default App;
