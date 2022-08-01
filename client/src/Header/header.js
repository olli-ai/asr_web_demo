import React from 'react';
import logo from './logo_red.png';

import { makeStyles } from "@material-ui/core/styles";


const useStyles = makeStyles(theme => ({
    logo: {
        width: "80px"
    }
}));

function Header() {
    const classes = useStyles();

    return (
        <div className="header col-12 text-center border-bottom border-3 border-secondary pb-2 mb-4" >
            <h1>Model Deployment <img className={classes.logo} src={logo} alt="Logo" /></h1>
        </div >
    );
}

export default Header;