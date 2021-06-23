import React from "react";
import './Navbar.css';

const Navbar = () => {
    return(
        <div>
            <header className="navbar">
                <h2>Your All in one News</h2>
                    <div className="signup">
                        <input className="email ma1-r" type="email" placeholder="Enter email"/>
                        <input className="subscribe f6 link dib white bg-light-purple grow" type="submit"  value="Subscribe"/>

                            {/* <legend className="pa0 f5 f4-ns mb3 black-80">Sign up for our newsletter</legend>
                            <div className="cf">
                                <input className="f6 f5-l input-reset b--black bn fl black-80 bg-white 
                                pa3 lh-solid w-100 w-75-m w-80-l br2-ns br--left-ns" placeholder="Your Email Address"
                                 type="text" name="email-address" value="" id="email-address" />
                                
                            </div> */}   
                    </div>
            </header>
        </div>
    )
}

export default Navbar;