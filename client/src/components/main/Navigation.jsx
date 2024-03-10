import React from "react";
import { FaHome } from "react-icons/fa";
import { IoIosArrowForward } from "react-icons/io";
import { Link } from "react-router-dom";

const Navigation = ({ title }) => {
  return (
    <div className="wrap mt-4">
      <div className="flex gap-2 items-center">
        <Link to="/" className="flex items-center gap-1">
          <FaHome />
          Home
        </Link>
        <IoIosArrowForward />
        <b>{title}</b>
      </div>
    </div>
  );
};

export default Navigation;
