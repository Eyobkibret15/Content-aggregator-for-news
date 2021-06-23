import React from "react";
// import './Navbar.css';

const HackerNews = ({ newsList }) => {
    // console.log(newsList);
    return(
        <div className="bg-gray">
            <h2>HackerNews</h2>
           <div>
               <a href={newsList.titlelink[0]}>{newsList.title[0]}</a>
            </div>
            <div>
                <a href="#">{newsList.detail[0]}</a><br/>
                <a href={newsList.commentlink[0]}>{newsList.comment[0]}</a><br/> 
            </div>
            <div>
               <a href={newsList.titlelink[1]}>{newsList.title[1]}</a>
            </div>
            <div>
                <a href="#">{newsList.detail[1]}</a><br/>
                <a href={newsList.commentlink[1]}>{newsList.comment[1]}</a><br/> 
            </div>
            <div>
               <a href={newsList.titlelink[2]}>{newsList.title[2]}</a>
            </div>
            <div>
                <a href="#">{newsList.detail[2]}</a><br/>
                <a href={newsList.commentlink[2]}>{newsList.comment[2]}</a><br/> 
            </div>
            <div>
               <a href={newsList.titlelink[3]}>{newsList.title[3]}</a>
            </div>
            <div>
                <a href="#">{newsList.detail[3]}</a><br/>
                <a href={newsList.commentlink[3]}>{newsList.comment[3]}</a><br/> 
            </div>
            <div>
               <a href={newsList.titlelink[4]}>{newsList.title[4]}</a>
            </div>
            <div>
                <a href="#">{newsList.detail[4]}</a><br/>
                <a href={newsList.commentlink[4]}>{newsList.comment[4]}</a><br/> 
            </div>
        </div>
    )
}

export default HackerNews;