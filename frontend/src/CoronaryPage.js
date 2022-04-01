import React, {useState} from 'react'
import {FormInputDropdown, FormNumberInput, ErrorMessage, Submit} from './Components'
import {useForm} from "react-hook-form";

function DiabetesPage() {
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


        // values will be passed to Flask concurrently, not here

    }

    const options_Gender = [
        { label: "Male", value: "1", },
        { label: "Female", value: "2", },
    ];

    const options_ChestPainType = [
        { label: "Atypical Angina", value: "1", },
        { label: "Typical Angina", value: "2", },
        { label: "Non-anginal Pain", value: "3", },
        { label: "Asymptomatic", value: "4", },
    ];

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <div className="DiabetesPage">
                <FormNumberInput name={'Age'} control={control} question="What is the patient's age?" register={register}/>
                <FormInputDropdown name={'Gender'} control={control} question="What is the patient's gender?" options={options_Gender} register={register}/>
                <FormInputDropdown name={'ChestPainType'} control={control} question="Did patient" options={options_ChestPainType} register={register}/>
                <FormNumberInput name={'RestingBloodPressure'} control={control} question='Did the patient also suffer from ... previously?' register={register}/>
                <Submit reset={reset}/>
                <ErrorMessage error={error}/>
            </div>
        </form>
    );
}

export default DiabetesPage;
