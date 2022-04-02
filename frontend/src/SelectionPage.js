import React, {useState} from 'react'
import {SelectSurvey} from './Components'
import stroke from "./stroke.png";
import coronary from "./coronary.png";
import diabetes from "./diabetes.png";
import cataracts from "./cataracts.png";
import pneumonia from "./pneumonia.png"

function SelectionPage() {
    return (
        <div style={{display: 'flex', flexDirection: 'row', flexWrap: 'wrap', justifyContent:'space-between', alignContent:'space-between', height:'45vh', width:'55vh'}}>
            <SelectSurvey name="Diabetes" imgLink={diabetes} pathLink={'/diabetes'}/>
            <SelectSurvey name="Coronary Artery Disease" imgLink={coronary} pathLink={'/coronary'}/>
            <SelectSurvey name="Stroke" imgLink={stroke} pathLink={'/stroke'}/>
            <SelectSurvey name="Cataracts" imgLink={cataracts} pathLink={'/cataracts'}/>
            <SelectSurvey name="Pneumonia" imgLink={pneumonia} pathLink={'/pneumonia'}/>
            <SelectSurvey name="Disease" imgLink={stroke} pathLink={'/diabetes'}/>
        </div>


    );

}

export default SelectionPage;
