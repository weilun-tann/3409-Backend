import React, {useEffect, useState} from "react";
import PropTypes from 'prop-types';
import {Backdrop, Box, Button, MenuItem, Select, Slider, TextField, Typography} from "@material-ui/core";
import { Uploader } from 'rsuite';
import {Controller} from "react-hook-form";
import Modal from '@mui/material/Modal';
import { useSpring, animated } from 'react-spring';
import {useNavigate} from "react-router-dom";

// selection icons for survey
export const SelectSurvey =({name, imgLink, pathLink}) => {
    let navigate = useNavigate();
    const [bgColour, setBgColour] = useState("#f2f2f2")
    const [txtColour, setTxtColour] = useState("#f2f2f2")
    return(
        <div onClick={()=>navigate(pathLink)} style={{cursor:'pointer', width: '17vh',backgroundColor:bgColour, borderRadius: '10px', paddingTop:'10px', paddingBottom:'10px', boxShadow: '2px 3px 2px lightgrey' }} onMouseEnter={() =>{setBgColour("#81a9e5"); setTxtColour("#f7f7fd")} } onMouseLeave={() => {setBgColour("#f2f2f2"); setTxtColour("#f2f2f2")}}>
            <img src={imgLink} onClick={()=>navigate(pathLink)} style={{width:'15vh', height:'15vh', borderRadius: '10px',backgroundColor:txtColour, }}/>
            <div style={{ marginLeft:'4px', marginRight:'4px', height:'4vh', display:'flex', flexDirection:'row', alignItems:'center', justifyContent:'center'}} >
                <text style={{width:'15vh'}}>{name}</text>
            </div>

        </div>
        )
}

// Uploader
export const ImageUploader =({name, control, register}) => {
    const [selectedImage, setImage] = useState(null);

    const getImgURL = (img) => {
        if (img) {
            return URL.createObjectURL(selectedImage)
        } else {
            return ''
        }
    };

    return <Controller
        name={name}
        control={control}
        defaultValue={null}
        render={({ field: { onChange, value } }) => (
            <div style={{border:'2px grey dashed', borderRadius:'10px', width: '30vw', minHeight:'10vh', display:'flex', flexDirection:'column', padding:'10px',justifyContent:'center', alignItems:'center'}}>
                <input type='file' value={selectedImage} onChange={onChange}
                       accept=".png,.jpg,.jpeg" />
                <img src={ getImgURL(selectedImage) } style={{maxHeight:'45vh', maxWidth:'30vw'}} />
            </div>
        )}
        {...register(name)}
    />
}

// Form Dropdown Input
export const FormInputDropdown= ({name, question, options, control, register}) => {
    const generateSelectOptions = () => {
        return options.map((option) => {
            return (
                <MenuItem key={option.value} value={option.value}>
                    {option.label}
                </MenuItem>
            );
        });
    };

    return <Controller
        name={name}
        control={control}
        defaultValue={null}
        render={({ field: { onChange, value } }) => (
            <div style={{width:'30vw', flexDirection: 'column', display:'flex' }}>
                <a style={{width:'30vw', marginBottom:'12px', marginTop:'20px', textAlign:'left'}}>{question}</a>
                <Select onChange={onChange} value={value} style={{marginBottom:'10px'}}>
                    {generateSelectOptions()}
                </Select>
            </div>
        )}
        {...register(name)}
    />
};

// Numeric Input
export const FormNumberInput = ({name, question, control, register}) => {
    return <Controller
        name={name}
        control={control}
        defaultValue={''}
        render={({ field: { onChange, value } }) => (
            <div style={{width:'30vw', flexDirection: 'column', display:'flex'}}>
                <a style={{width:'30vw', marginBottom:'12px', marginTop:'20px', textAlign:'left'}}>{question}</a>
                <TextField onChange={onChange} value={value} id="number-input" label="Value" type="text" inputProps={{ inputMode: 'numeric', pattern: '[0-9]*' }} style={{marginBottom:'10px'}}/>
            </div>
        )}
        {...register(name)}
    />
};

// Numeric Input
export const ScaleSliderInput = ({name, question, control, range, register}) => {
    return <Controller
        name={name}
        control={control}
        defaultValue={''}
        render={({ field: { onChange, value } }) => (
            <div style={{width:'30vw', flexDirection: 'column', display:'flex'}}>
                <a style={{width:'30vw', marginBottom:'12px', marginTop:'20px', textAlign:'left'}}>{question}</a>
                <Slider
                    aria-label="Always visible"
                    defaultValue={1}
                    step={1}
                    min = {1}
                    max={range}
                    valueLabelDisplay="on"
                    style={{marginBottom:'10px', width:'25vw', alignSelf:'center', marginTop:'35px'}}/>
            </div>
        )}
        {...register(name)}
    />
};

// Submit and Reset Button
export const Submit = (reset) => {
    return (
        <div style={{width:'inherit', display: 'flex', justifyContent:'space-between', margin:'10px 0px', padding:'3px 0px'}}>
            <Button onClick={()=>console.log('Submit')} variant={"contained"} type="submit">
                {" "}Submit{" "}
            </Button>
            <Button onClick={()=>reset.reset()} variant={"outlined"}>
                {" "}Reset{" "}
            </Button>
        </div>
    );
};

// Pop-up for error
const Fade = React.forwardRef(function Fade(props, ref) {
    const { in: open, children, onEnter, onExited, ...other } = props;
    const style = useSpring({
        from: { opacity: 0 },
        to: { opacity: open ? 1 : 0 },
        onStart: () => {
            if (open && onEnter) {
                onEnter();
            }
        },
        onRest: () => {
            if (!open && onExited) {
                onExited();
            }
        },
    });

    return (
        <animated.div ref={ref} style={style} {...other}>
            {children}
        </animated.div>
    );
});

Fade.propTypes = {
    children: PropTypes.element,
    in: PropTypes.bool.isRequired,
    onEnter: PropTypes.func,
    onExited: PropTypes.func,
};

export const ErrorMessage = (error) =>  {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    useEffect(()=> {
        console.log(error)
        if (error.error){
            handleOpen()
        }
    },[error])

    return (
        <div >
            <Modal
                aria-labelledby="spring-modal-title"
                aria-describedby="spring-modal-description"
                open={open}
                onClose={handleClose}
                closeAfterTransition
                BackdropComponent={Backdrop}
                BackdropProps={{
                    timeout: 500,
                }}
                style={{
                }}
            >
                <Fade in={open} >
                    <Box style={{
                        padding: '25px',
                        backgroundColor: '#eeeeee',
                        width: "45vw",
                        height: "10vh",
                        border: '2px solid #000',
                        boxShadow: "24",
                        p: "4",
                        borderRadius: "10px",
                        position: 'absolute',
                        left: '0',
                        right: '0',
                        marginLeft: 'auto',
                        marginRight: 'auto',
                        top: '45vh',
                        bottom: '45vh',
                        marginTop: 'auto',
                        marginBottom: 'auto',
                        textAlign: "center", alignItems:'center', justifyContent:'center',
                        display:'flex'
                    }}>
                        <Typography id="spring-modal-title" variant="h6" component="h2" >
                            Kindly fill up all required fields before proceeding
                        </Typography>
                    </Box>
                </Fade>
            </Modal>
        </div>
    );
}
