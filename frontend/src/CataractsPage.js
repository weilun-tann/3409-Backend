import React, {useState} from 'react'
import {ErrorMessage, Submit, ImageUploader, AwaitResults} from './Components'
import {useForm} from "react-hook-form";
import {useNavigate} from "react-router-dom";

function CataractsPage() {
    const { register, handleSubmit, control, getValues, reset } = useForm();
    const [error, showError] = useState(false);
    const [query, changeQueryingState] = useState(false);
    let navigate = useNavigate();
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
            'https://ai-doctor-3409.herokuapp.com/predict/cataracts',
            {
                method: 'POST',
                body: values,
            }
        )
            .then((response) => response.json())
            .then((result) => {
                console.log('Success:', result.outcome);
                changeQueryingState(false);
                navigate('/results', { state: {prevPage: 'Cataracts', result: result.outcome} });
            })
            .catch((error) => {
                console.error('Error:', error);
                changeQueryingState(false);
                navigate('/results', { state: {prevPage: 'Cataracts', result: "Something went wrong... Try again later"} });
            });
    }


    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <div className="CataractsPage" style={{height:'75vh'}}>
                <ImageUploader name='cataracts' control={control} register={register}/>
                <Submit/>
                <ErrorMessage error={error}/>
                <AwaitResults waiting={query} />
            </div>
        </form>


    );

}

export default CataractsPage;
