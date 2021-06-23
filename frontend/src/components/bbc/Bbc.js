import React from "react";
// import './Navbar.css';

const Bbc = ({ newsList }) => {
    // console.log(newsList);
    return(
        <div className="bg-brown">
            <h2>BBC</h2>
           <div>
               <a href={newsList.titlelink[0]}>{newsList.title[0]}</a>
            </div>
            <div>
                <p>{newsList.detail[0]}</p><br/>
                <p>{newsList.location[0]}</p>
                <p>{newsList.time[0]}</p>
            </div>
            <div>
               <a href={newsList.titlelink[1]}>{newsList.title[1]}</a>
            </div>
            <div>
                <p>{newsList.detail[1]}</p><br/>
                <p>{newsList.location[1]}</p>
                <p>{newsList.time[1]}</p>
            </div>
            <div>
               <a href={newsList.titlelink[2]}>{newsList.title[2]}</a>
            </div>
            <div>
                <p>{newsList.detail[2]}</p><br/>
                <p>{newsList.location[2]}</p>
                <p>{newsList.time[2]}</p>
            </div>
            <div>
               <a href={newsList.titlelink[3]}>{newsList.title[3]}</a>
            </div>
            <div>
                <p>{newsList.detail[3]}</p><br/>
                <p>{newsList.location[3]}</p>
                <p>{newsList.time[3]}</p>
            </div>
            <div>
               <a href={newsList.titlelink[4]}>{newsList.title[4]}</a>
            </div>
            <div>
                <p>{newsList.detail[4]}</p><br/>
                <p>{newsList.location[4]}</p>
                <p>{newsList.time[4]}</p>
            </div>
        </div>
    )
}

export default Bbc;