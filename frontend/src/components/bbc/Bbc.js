import React from "react";
import './Bbc.css';
import { FcClock } from "react-icons/fc";


const Bbc = ({ newsList }) => {
    // console.log(newsList);
    return(
        <div className="">
            <h2>BBC</h2>
           <div>
               <a className="title" href={newsList.titlelink[0]}>{newsList.title[0]}</a>
            </div>
            <div>
                <p>{newsList.detail[0]}</p>
                <p className="gray">{newsList.location[0]} | <FcClock /> {newsList.time[0]}</p>
            </div>
            <hr />
            <div>
               <a className="title" href={newsList.titlelink[1]}>{newsList.title[1]}</a>
            </div>
            <div>
                <p>{newsList.detail[1]}</p>
                <p className="gray">{newsList.location[1]} | <FcClock />{newsList.time[1]}</p>
            </div>
            <hr />

            <div>
               <a className="title" href={newsList.titlelink[2]}>{newsList.title[2]}</a>
            </div>
            <div>
                <p>{newsList.detail[2]}</p>
                <p className="gray">{newsList.location[2]} | <FcClock />{newsList.time[2]}</p>
            </div>
            <hr />

            <div>
               <a className="title" href={newsList.titlelink[3]}>{newsList.title[3]}</a>
            </div>
            <div>
                <p>{newsList.detail[3]}</p>
                <p className="gray">{newsList.location[3]} | <FcClock />{newsList.time[3]}</p>
            </div>
            <hr />

            <div>
               <a className="title" href={newsList.titlelink[4]}>{newsList.title[4]}</a>
            </div>
            <div>
                <p>{newsList.detail[4]}</p>
                <p className="gray">{newsList.location[4]} | <FcClock /> {newsList.time[4]}</p>
            </div>
        </div>
    )
}

export default Bbc;