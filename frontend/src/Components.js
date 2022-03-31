import React, {useEffect} from "react";
import PropTypes from 'prop-types';
import {Backdrop, Box, Button, MenuItem, Select, TextField, Typography} from "@material-ui/core";
import {Controller} from "react-hook-form";
import Modal from '@mui/material/Modal';
import { useSpring, animated } from 'react-spring';


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
        render={({ field: { onChange, value } }) => (
            <div style={{width:'30vw', flexDirection: 'column', display:'flex' }}>
                <a style={{width:'30vw', marginBottom:'10px', marginTop:'20px', textAlign:'left'}}>{question}</a>
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
        render={({ field: { onChange, value } }) => (
            <div style={{width:'30vw', flexDirection: 'column', display:'flex'}}>
                <a style={{width:'30vw', marginBottom:'10px', marginTop:'20px', textAlign:'left'}}>{question}</a>
                <TextField onChange={onChange} value={value} id="number-input" label="Value" type="number" inputProps={{ inputMode: 'numeric', pattern: '[0-9]*' }} style={{marginBottom:'10px'}}/>
            </div>
        )}
        {...register(name)}
    />
};

// Submit and Reset Button
export const Submit = () => {
    return (
        <div style={{width:'30vw', display: 'flex', justifyContent:'space-between', margin:'10px 0px'}}>
            <Button onClick={()=>console.log('Submit')} variant={"contained"} type="submit">
                {" "}Submit{" "}
            </Button>
            <Button onClick={() => console.log('Reset')} variant={"outlined"}>
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
                style={{textAlign: 'center',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',}}
            >
                <Fade in={open} >
                    <Box style={{
                        padding: '25px',
                        backgroundColor: '#eeeeee',
                        width: "45vw",
                        border: '2px solid #000',
                        boxShadow: "24",
                        p: "4",
                        borderRadius: "15px"
                    }}>
                        <Typography id="spring-modal-title" variant="h6" component="h2" style={{textAlign: "center", flexDirection:'overflow'}}>
                            Kindly fill up all required fields before proceeding
                        </Typography>
                    </Box>
                </Fade>
            </Modal>
        </div>
    );
}
