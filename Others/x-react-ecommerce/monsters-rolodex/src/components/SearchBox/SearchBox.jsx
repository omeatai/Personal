import React from "react";
import "./SearchBox.css";

const SearchBox = ({ type, className, placeholder, value, handleSearch }) => {
  return (
    <section>
      <input
        type={type}
        className={className}
        placeholder={placeholder}
        value={value}
        onChange={handleSearch}
      />
    </section>
  );
};
export default SearchBox;
