import React from "react";
import { FcClock } from "react-icons/fc";

import './Tvn24.css';

const Tvn24 = ({ newsList }) => {
    // console.log(newsList);
    return(
        <div className="">
            <h2>Tvn24</h2>
           <div>
               <a className="title" href={newsList.titlelink[0]}>{newsList.title[0]}</a>
            </div>
            <div>
                <a className="detail" href={newsList.detaillink[0]}>{newsList.detail[0]}</a><br/>
                <h3><FcClock className="mr2" />{newsList.time[0]}</h3>
            </div>
            <div>
               <a className="title" href={newsList.titlelink[1]}>{newsList.title[1]}</a>
            </div>
            <div>
                <a className="detail" href={newsList.detaillink[1]}>{newsList.detail[1]}</a><br/>
                <h3><FcClock className="mr2" /> {newsList.time[1]}</h3>
            </div><div>
               <a className="title" href={newsList.titlelink[2]}>{newsList.title[2]}</a>
            </div>
            <div>
                <a className="detail" href={newsList.detaillink[2]}>{newsList.detail[2]}</a><br/>
                <h3><FcClock className="mr2" />{newsList.time[2]}</h3>
            </div><div>
               <a className="title" href={newsList.titlelink[3]}>{newsList.title[3]}</a>
            </div>
            <div>
                <a className="detail" href={newsList.detaillink[3]}>{newsList.detail[3]}</a><br/>
                <h3><FcClock className="mr2" />{newsList.time[3]}</h3>
            </div><div>
               <a className="title" href={newsList.titlelink[4]}>{newsList.title[4]}</a>
            </div>
            <div>
                <a className="detail" href={newsList.detaillink[4]}>{newsList.detail[4]}</a><br/>
                <h3><FcClock className="mr2" /> {newsList.time[4].slice(-4)}</h3>
            </div>
        </div>
    )
}

export default Tvn24;