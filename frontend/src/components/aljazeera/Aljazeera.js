import React from "react";
import './Aljazeera.css';

const Aljazeera = ({ newsList }) => {
    // console.log(newsList);
    return(
        <div className="aljazeera">
            <h2>Aljazeera</h2>
           <div className="titlediv">
               <a className="aljazeeraTitle" href={newsList.titlelink[0]}>{newsList.title[0]}</a>
            </div>
            <div>
                <a className="detail" href={newsList.detaillink[0]}>{newsList.detail[0]}</a>
                {/* <p>{newsList.time[0]}</p> */}
            </div>
             <div>
               <a className="aljazeeraTitle" href={newsList.titlelink[1]}>{newsList.title[1]}</a>
            </div>
            <div>
                <a className="detail" href={newsList.detaillink[1]}>{newsList.detail[1]}</a>
            </div> 
            <div>
               <a className="aljazeeraTitle" href={newsList.titlelink[2]}>{newsList.title[2]}</a>
            </div>
            <div>
                <a className="detail" href={newsList.detaillink[2]}>{newsList.detail[2]}</a>
            </div>
             <div>
               <a className="aljazeeraTitle" href={newsList.titlelink[3]}>{newsList.title[3]}</a>
            </div>
            <div>
                <a className="detail" href={newsList.detaillink[3]}>{newsList.detail[3]}</a>
            </div>
            <div>
               <a className="aljazeeraTitle" href={newsList.titlelink[3]}>{newsList.title[3]}</a>
            </div>
            <div>
                <a className="detail" href={newsList.detaillink[3]}>{newsList.detail[3]}</a>
            </div>
        </div>
    )
}

export default Aljazeera;