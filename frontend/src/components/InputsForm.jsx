import { Button, Paper, Typography } from "@material-ui/core";
import { FormProvider, useForm } from "react-hook-form";
import { FormInputText } from "./form-components/FormInputText";
import { FormInputMultiCheckbox } from "./form-components/FormInputMultiCheckbox";
import { FormInputDropdown } from "./form-components/FormInputDropdown";
import { FormInputDate } from "./form-components/FormInputDate";
import { FormInputSlider } from "./form-components/FormInputSlider";

const defaultValues = {
  textValue: "",
  radioValue: "",
  checkboxValue: [],
  dateValue: new Date(),
  dropdownValue: "",
  sliderValue: 0,
};

export const InputsForm = () => {
  const methods = useForm({ defaultValues: defaultValues });
  const { handleSubmit, reset, control, setValue } = methods;
  const onSubmit = (data) => console.log(data);

  return (
    <Paper>
      <Typography variant="h6"> Inputs Form </Typography>

      <FormInputText name="textValue" control={control} label="Text Input" />
      <FormInputDropdown name="dropdownValue"control={control}label="Dropdown Input"/>
      <FormInputDate name="dateValue" control={control} label="Date Input" />

      <FormInputMultiCheckbox
        control={control}
        setValue={setValue}
        name={"checkboxValue"}
        label={"Checkbox Input"}
      />

      <FormInputSlider
        name={"sliderValue"}
        control={control}
        setValue={setValue}
        label={"Slider Input"}
      />

      <Button onClick={handleSubmit(onSubmit)} variant={"contained"}>
        Submit
      </Button>
      <Button onClick={() => reset()} variant={"outlined"}>
        Reset
      </Button>
    </Paper>
  );
};