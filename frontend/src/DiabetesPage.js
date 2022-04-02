import React, {useState} from 'react'
import {FormInputDropdown, FormNumberInput, ErrorMessage, Submit, ScaleSliderInput} from './Components'
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
        reset();
        return;


        // values will be passed to Flask concurrently, not here

    }
    const options_Sex = [
        { label: "Male", value: "1", },
        { label: "Female", value: "2", },
    ];

    const options_Hypertension = [
        { label: "Present", value: "1", },
        { label: "Absent", value: "2", },
    ];

    const options_HighCholesterol = [
        { label: "High", value: "1", },
        { label: "Normal", value: "2", },
    ];

    const options_Smoking = [
        { label: "Smokes", value: "1", },
        { label: "Formerly smoked", value: "1", },
        { label: "Never smoked", value: "2", },
    ];

    const options_Stroke = [
        { label: "Previously", value: "1", },
        { label: "Never", value: "2", },
    ];

    const options_CoronaryArteryDisease = [
        { label: "Yes", value: "1", },
        { label: "No", value: "2", },
    ];

    const options_Lifestyle = [
        { label: "Active", value: "1", },
        { label: "Normal", value: "2", },
    ];

    const options_FruitsConsumption = [
        { label: "Active", value: "1", },
        { label: "Normal", value: "2", },
    ];

    const options_VegetableConsumption = [
        { label: "Active", value: "1", },
        { label: "Normal", value: "2", },
    ];

    const options_AlcoholConsumption = [
        { label: "Active", value: "1", },
        { label: "Normal", value: "2", },
    ];

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <div className="DiabetesPage" style={{height:'75vh'}}>
                <FormNumberInput name={'Age'} control={control} question="What is the patient's age?" register={register}/>
                <FormInputDropdown name={'Sex'} control={control} question="What is the patient's gender?" options={options_Sex} register={register}/>
                <FormNumberInput name={'Income'} control={control} question="What is the patient's income?" register={register}/>
                <FormInputDropdown name={'Hypertension'} control={control} question='Does patient have a history of hypertension?' options={options_Hypertension} register={register}/>
                <FormInputDropdown name={'HighCholesterol'} control={control} question='Does patient have a history of high cholesterol?' options={options_HighCholesterol} register={register}/>
                <FormNumberInput name={'BMI'} control={control} question="What is the patient's BMI level?" register={register}/>
                <FormInputDropdown name={'SmokingStatus'} control={control} question="Is patient a smoker or has ever smoked before?" options={options_Smoking} register={register}/>
                <FormInputDropdown name={'Stroke'} control={control} question="Did patient suffer from stroke before?" options={options_Stroke} register={register}/>
                <FormInputDropdown name={'Coronary'} control={control} question="Is patient diagnosed with any form of coronary artery disease?" options={options_CoronaryArteryDisease} register={register}/>
                <FormInputDropdown name={'Lifestyle'} control={control} question="Did patient suffer from stroke before?" options={options_Lifestyle} register={register}/>
                <FormInputDropdown name={'FruitsConsumption'} control={control} question="What is the level of patient's fruit consumption?" options={options_FruitsConsumption} register={register}/>
                <FormInputDropdown name={'VegetableConsumption'} control={control} question="What is the level of patient's vegetable consumption?" options={options_VegetableConsumption} register={register}/>
                <FormInputDropdown name={'AlcoholConsumption'} control={control} question="What is the level of patient's alcohol consumption?" options={options_AlcoholConsumption} register={register}/>
                <ScaleSliderInput name={'GeneralHealth'} control={control} question="What is the general condition of patient's overall health?" range={5} register={register}/>
                <Submit reset={reset}/>
                <ErrorMessage error={error}/>

            </div>
        </form>


    );

}

export default DiabetesPage;
