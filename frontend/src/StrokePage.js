import React, {useState} from 'react'
import {FormInputDropdown, FormNumberInput, ErrorMessage, Submit} from './Components'
import {useForm} from "react-hook-form";

function StrokePage() {
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

    const options_Gender = [
        { label: "Male", value: "1", },
        { label: "Female", value: "2", },
    ];

    const options_Hypertension = [
        { label: "Present", value: "1", },
        { label: "Absent", value: "2", },
    ];

    const options_CoronaryArteryDisease = [
        { label: "Present", value: "1", },
        { label: "Absent", value: "2", },
    ];

    const options_Smoking = [
        { label: "Smokes", value: "1", },
        { label: "Formerly smoked", value: "2", },
        { label: "Never smoked", value: "3", },
    ];

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <div className="StrokePage">
                <FormInputDropdown name={'Gender'} control={control} question="What is the patient's gender?" options={options_Gender} register={register}/>
                <FormNumberInput name={'Age'} control={control} question="What is the patient's age?" register={register}/>
                <FormInputDropdown name={'Hypertension'} control={control} question="Does patient have a history of hypertension?" options={options_Hypertension} register={register}/>
                <FormInputDropdown name={'CoronaryArteryDisease'} control={control} question="Does patient have a history of coronary artery disease?" options={options_CoronaryArteryDisease} register={register}/>
                <FormNumberInput name={'GlucoseLevel'} control={control} question="What is the patient's average glucose level (mg/dL)?" register={register}/>
                <FormNumberInput name={'BMI'} control={control} question="What is the patient's BMI level?" register={register}/>
                <FormInputDropdown name={'SmokingStatus'} control={control} question="Is patient a smoker or has ever smoked before?" options={options_Smoking} register={register}/>
                <Submit reset={reset}/>
                <ErrorMessage error={error}/>
            </div>
        </form>
    );

}

export default StrokePage;
