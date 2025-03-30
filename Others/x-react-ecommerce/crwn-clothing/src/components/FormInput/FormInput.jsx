import React from "react";
import { FormInputLabel, Input, Group } from "./FormInputStyle.js";

const FormInput = ({ label, ...otherProps }) => {
  return (
    <Group>
      <Input {...otherProps} />
      {label && (
        <FormInputLabel
          shrink={otherProps.value.length}
          htmlFor={`${otherProps.id}`}
          // className={`${
          //   otherProps.value.length ? "shrink" : ""
          // } form-input-label`}
        >
          {label}
        </FormInputLabel>
      )}
    </Group>
  );
};

export default FormInput;
