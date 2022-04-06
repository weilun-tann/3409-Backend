import React from 'react'
import {useLocation} from "react-router-dom";

function ResultsPage() {
    const location = useLocation();
    console.log(location.state);
    return (

        <div className="ResultsPage" style={{height:'75vh', width:'30vw'}}>

            <h1>Results Page</h1>

            <div>{location.state.prevPage}</div>
            <div>{location.state.result}</div>

        </div>

    );

}

export default ResultsPage;
