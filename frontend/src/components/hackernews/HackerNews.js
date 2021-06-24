import React from "react";
import './HackerNews.css';
import { FcComments } from "react-icons/fc";
import { FcClock } from "react-icons/fc";


const HackerNews = ({ newsList }) => {
    // console.log(newsList);
    return(
        <div className="hackerNews">
            <h2>HackerNews</h2>
           <div>
               <a className="title" href={newsList.titlelink[0]}>{newsList.title[0]}</a>
            </div>
            <div>
                <a className="detail" href="#">{newsList.detail[0].slice(0,-12)}</a><br/>
                <a className="comment mr5" href={newsList.commentlink[0]}><FcComments />{newsList.comment[0].slice(0,-9)}</a><a><FcClock />{newsList.detail[0].slice(-11)}</a>
            </div>
            <hr/>
            <div>
               <a className="title" href={newsList.titlelink[1]}>{newsList.title[1]}</a>
            </div>
            <div>
                <a className="detail" href="#">{newsList.detail[1]}</a><br/>
                <a className="comment mr5" href={newsList.commentlink[1]}><FcComments />{newsList.comment[1].slice(0,-9)}</a><a><FcClock />{newsList.detail[0].slice(-11)}</a>
            </div>
            <hr/>
            <div>
               <a className="title" href={newsList.titlelink[2]}>{newsList.title[2]}</a>
            </div>
            <div>
                <a  className="detail" href="#">{newsList.detail[2]}</a><br/>
                <a className="comment mr5" href={newsList.commentlink[2]}><FcComments />{newsList.comment[2].slice(0,-9)}</a><a><FcClock />{newsList.detail[0].slice(-12)}</a> 
            </div>
            <hr/>
            <div>
               <a className="title" href={newsList.titlelink[3]}>{newsList.title[3]}</a>
            </div>
            <div>
                <a className="detail"  href="#">{newsList.detail[3]}</a><br/>
                <a className="comment mr5" href={newsList.commentlink[3]}><FcComments />{newsList.comment[3].slice(0,-9)}</a><a><FcClock />{newsList.detail[0].slice(0,-12)}</a>
            </div>
            <hr/>
            <div>
               <a  className="title" href={newsList.titlelink[4]}>{newsList.title[4]}</a>
            </div>
            <div>
                <a className="detail" href="#">{newsList.detail[4]}</a><br/>
                <a className="comment mr5" href={newsList.commentlink[4]}><FcComments />{newsList.comment[4].slice(0,-9)}</a><a><FcClock />{newsList.detail[0].slice(-12)}</a>
            </div>
        </div>
    )
}

export default HackerNews;