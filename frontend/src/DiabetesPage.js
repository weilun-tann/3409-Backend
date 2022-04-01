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
        reset();
        return;


        // values will be passed to Flask concurrently, not here

    }

    const options_1 = [
        { label: "Yes", value: "1", },
        { label: "No", value: "2", },
    ];

    const options_2 = [
        { label: "Yes", value: "1", },
        { label: "No", value: "2", },
    ];

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <div className="DiabetesPage">

                <FormInputDropdown name={'test_1'} control={control} question='Did the patient suffer from ... previously?' options={options_1} register={register}/>
                <FormNumberInput name={'test_2'} control={control} question='Did the patient also suffer from ... previously?' register={register}/>
                <Submit/>
                <ErrorMessage error={error}/>

            </div>
        </form>


    );

}

export default DiabetesPage;
