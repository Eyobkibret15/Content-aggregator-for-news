import React from "react";
import './Navbar.css';

const Navbar = () => {
    return(
        <div>
            <header className="navbar">
                <h2>Your All in one News</h2>
                    <div className="signup">
                        {/* <input className="email ma1-r" type="email" placeholder="Enter email"/> */}
                        {/* <input className="subscribe f6 link dib white bg-light-purple grow" type="submit"  value="Subscribe"/> */}
                        <h2>{new Date().toLocaleString()}</h2>
                    </div>
            </header>
        </div>
    )
}

export default Navbar;