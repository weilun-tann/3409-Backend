import React, {useState} from 'react'
import {ErrorMessage, Submit, AudioUploader} from './Components'
import {useForm} from "react-hook-form";

function RespiratoryPage() {
    const { register, handleSubmit, control, getValues, reset } = useForm();
    const [error, showError] = useState(false);
    const onSubmit = (values) =>{
        for (var key in values) {
            if (values[key]===undefined || values[key]===''){
                console.log(key);
                showError(true);
                showError(false); // this is to reinitialize to false
                return;
            }
        }
        fetch(
            'https://ai-doctor-3409.herokuapp.com/predict/respiratory?' + new URLSearchParams(values),
            {
                method: 'POST',
                body: values,
            }
        )
            .then((response) => response.json())
            .then((result) => {
                console.log('Success:', result);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <div className="RespiratoryPage" style={{height:'75vh'}}>
                <AudioUploader name='respiratory' control={control} register={register}/>
                <Submit/>
                <ErrorMessage error={error}/>

            </div>
        </form>


    );

}

export default RespiratoryPage;
