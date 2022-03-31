import React, {useState} from 'react'
import {FormInputDropdown, FormNumberInput, ErrorMessage, Submit} from './Components'
import {useForm} from "react-hook-form";
import {Link} from "react-router-dom";

function SelectionPage() {


    return (
        <div>
            <ul>
                <li> <Link to="/diabetes">About</Link> </li>
                <li> <Link to="/topics">Topics</Link> </li>
            </ul>
        </div>


    );

}

export default SelectionPage;
