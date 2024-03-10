import React from "react";
import Heading from "./Heading.jsx";
import { Link } from "react-router-dom";
import { IoMenu } from "react-icons/io5";
import HeadingMobile from "./HeadingMobile.jsx";

const Header = () => {
  return (
    <header className="w-full">
      <HeadingMobile />
      <div className=" flex">
        <Heading />
      </div>
      <nav className=" text-white bg-[#333333] hidden md:block">
        <ul className=" wrap flex justify-center py-2 gap-10">
          <Link to="/filter/all" className="nav-item">
            All
          </Link>
          <Link to="/filter/sales" className="nav-item">
            SALES
          </Link>
          <Link to="/filter/nike" className="nav-item">
            NIKE
          </Link>
          <Link to="/filter/vans" className="nav-item">
            VANS
          </Link>
          <Link to="/filter/converse" className="nav-item">
            CONVERSE
          </Link>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
