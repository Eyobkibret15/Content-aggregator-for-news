import React from "react";
import './App.css';

import Navbar from './components/Navbar/Navbar'
import Aljazeera from './components/aljazeera/Aljazeera';
import Bbc from './components/bbc/Bbc';
import FirstNews from './components/firstnews/FirstNews';
import HackerNews from './components/hackernews/HackerNews';
import Tvn24 from './components/tvn24/Tvn24';
import Footer from './components/Footer/Footer';


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
          <div><FirstNews newsList={this.state.allNews.firstnews} /></div>
          <div><Tvn24 newsList={this.state.allNews.tvn24} /></div>
          <div><Aljazeera newsList={this.state.allNews.aljazeera} /></div>
          <div><HackerNews newsList={this.state.allNews.hackernews} /></div>
          <div><Bbc newsList={this.state.allNews.bbc} /></div>
        </div>
         : 'Loading ...'}
      </div>      
      <Footer />
    </div>
  );
}
}

export default App;
