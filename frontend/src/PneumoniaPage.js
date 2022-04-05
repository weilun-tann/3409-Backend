import React, {useState} from 'react'
import {ErrorMessage, Submit, ImageUploader} from './Components'
import {useForm} from "react-hook-form";

function PneumoniaPage() {
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
            'https://ai-doctor-3409.herokuapp.com/predict/pneumonia?' + new URLSearchParams(values),
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
            <div className="PneumoniaPage" style={{height:'75vh'}}>
                <ImageUploader name='pneumonia' control={control} register={register}/>
                <Submit/>
                <ErrorMessage error={error}/>
            </div>
        </form>


    );

}

export default PneumoniaPage;
