import React from "react";

const FormInput = ({
  type,
  name,
  value,
  onChange,
  placeholder,
  required = true,
}) => {
  return (
    <div>
      <input
        type={type}
        name={name}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-purple-500 focus:border-purple-500"
        required={required}
      />
    </div>
  );
};

export default FormInput;
