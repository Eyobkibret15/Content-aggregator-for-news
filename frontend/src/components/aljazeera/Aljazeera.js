import React from "react";
// import './Navbar.css';

const Aljazeera = ({ newsList }) => {
    // console.log(newsList);
    return(
        <div>
            <h2>Aljazeera</h2>
           <div>
               <a className="link b grow" href={newsList.titlelink[0]}>{newsList.title[0]}</a>
            </div>
            <div>
                <a href={newsList.detaillink[0]}>{newsList.detail[0]}</a>
            </div>
             <div>
               <a className="link b grow" href={newsList.titlelink[1]}>{newsList.title[1]}</a>
            </div>
            <div>
                <a href={newsList.detaillink[1]}>{newsList.detail[1]}</a>
            </div> 
            <div>
               <a className="link b grow" href={newsList.titlelink[2]}>{newsList.title[2]}</a>
            </div>
            <div>
                <a href={newsList.detaillink[2]}>{newsList.detail[2]}</a>
            </div>
             <div>
               <a className="link b grow" href={newsList.titlelink[3]}>{newsList.title[3]}</a>
            </div>
            <div>
                <a href={newsList.detaillink[3]}>{newsList.detail[3]}</a>
            </div>
            <div>
               <a className="link b grow" href={newsList.titlelink[3]}>{newsList.title[3]}</a>
            </div>
            <div>
                <a href={newsList.detaillink[3]}>{newsList.detail[3]}</a>
            </div>
        </div>
    )
}

export default Aljazeera;