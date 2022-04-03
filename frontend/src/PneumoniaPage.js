import React, {useState} from 'react'
import {ErrorMessage, Submit, AudioUploader} from './Components'
import {useForm} from "react-hook-form";

function PneumoniaPage() {
    const { register, handleSubmit, control, getValues, reset } = useForm();
    const [error, showError] = useState(false);
    const onSubmit = (values) =>{
        console.log(values);
        for (var key in values) {
            if (values[key]===undefined || values[key]===''){
                console.log(key);
                showError(true);
                showError(false); // this is to reinitialize to false
                return;
            }
        }
        reset();
        return;


        // values will be passed to Flask concurrently, not here

    }

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <div className="PneumoniaPage">
                <AudioUploader name='pneumonia' control={control} register={register}/>
                <Submit reset={reset}/>
                <ErrorMessage error={error}/>

            </div>
        </form>


    );

}

export default PneumoniaPage;
