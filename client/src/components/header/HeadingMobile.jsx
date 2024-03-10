import React from "react";
import { FaAddressBook } from "react-icons/fa";
import { IoIosPersonAdd } from "react-icons/io";
import { Link } from "react-router-dom";

const HeadingMobile = () => {
  return (
    <div className="flex px-4 lg:hidden justify-end">
      <div className="relative group">
        <div className="flex items-center gap-1">
          <FaAddressBook /> Account
        </div>

        <div className="bg-white">
          <div className="opacity-0 hidden group-hover:block group-hover:opacity-100 transition-opacity duration-1000 absolute w-[150px] p-4 top-[90%] z-100 right-0 shadow-2xl bg-white rounded-sm">
            <div className="flex gap-2 items-center cursor-pointer">
              <IoIosPersonAdd />
              <Link to="register">Sign up</Link>
            </div>
            <div className="flex gap-2 items-center cursor-pointer">
              <FaAddressBook />
              <Link to="login">Sign in</Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HeadingMobile;
