import React from 'react';
import Select from 'react-select';

const ComboBox = ({ options, onChange }) => {
  return (
    <Select
      options={options}
      onChange={onChange}
      className="w-full"
    />
  );
};

export default ComboBox;
