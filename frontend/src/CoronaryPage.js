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

    const options_FastingBloodSugar = [
        { label: "Less than or equal to 120 mg/dl", value: "1", },
        { label: "More than 120 mg/dl", value: "2", },
    ];

    const options_RestingECG = [
        { label: "ST-T wave abnormality", value: "1", },
        { label: "Probable or definite left ventricular hypertrophy", value: "2", },
        { label: "Normal", value: "3", },
    ];

    const options_ExerciseInducedAngina = [
        { label: "Yes", value: "1", },
        { label: "No", value: "2", },
    ];

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <div className="CoronaryPage" >
                <FormNumberInput name={'Age'} control={control} question="What is the patient's age?" register={register}/>
                <FormInputDropdown name={'Gender'} control={control} question="What is the patient's gender?" options={options_Gender} register={register}/>
                <FormInputDropdown name={'ChestPainType'} control={control} question="What kind of chest pain does patient suffer from, if any?" options={options_ChestPainType} register={register}/>
                <FormNumberInput name={'RestingBloodPressure'} control={control} question="What is the patient's resting blood pressure (mm Hg)?" register={register}/>
                <FormNumberInput name={'Cholesterol'} control={control} question="What is the patient's average cholesterol level (mm/dL)?" register={register}/>
                <FormInputDropdown name={'FastingBloodSugar'} control={control} question="What is the level of fasting blood sugar level of patient (mg/dl)?" options={options_FastingBloodSugar} register={register}/>
                <FormInputDropdown name={'RestingECG'} control={control} question="What is the pattern of patient's resting ECG?" options={options_RestingECG} register={register}/>
                <FormNumberInput name={'MaxHR'} control={control} question="What is the patient's maximum heart rate (bps)?" register={register}/>
                <FormInputDropdown name={'ExerciseInducedAngina'} control={control} question="Does patient suffer from exercise induced angina?" options={options_ExerciseInducedAngina} register={register}/>
                <Submit reset={reset}/>
                <ErrorMessage error={error}/>
            </div>
        </form>
    );
}

export default DiabetesPage;
