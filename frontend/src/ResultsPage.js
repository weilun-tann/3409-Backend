import React, {useState} from 'react'
import {ErrorMessage, Submit, ImageUploader} from './Components'
import {useForm} from "react-hook-form";

function ResultsPage() {
    const [error, showError] = useState(false);

    return (

        <div className="ResultsPage" style={{height:'75vh'}}>
            <text>{}</text>
        </div>



    );

}

export default ResultsPage;
