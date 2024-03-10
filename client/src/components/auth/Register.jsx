import React, { useState } from "react";
import Navigation from "../main/Navigation";
import { Link, useNavigate } from "react-router-dom";
import { register_request } from "../../api/index.js";
import { toast } from "react-toastify";
import Loading from "../Loading.jsx";

const init = {
  last_name: "",
  first_name: "",
  email: "",
  password: "",
};



const Register = () => {
  const [data, setData] = useState(init);
  const [errorEmail, setErrorEmail] = useState("")
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    name == "email" && setErrorEmail("")
    setData({ ...data, [name]: value });
  };

  
  const handleRegister = async (e) => {
    // Add your login logic here  
    e.preventDefault()
    const { email, password, first_name, last_name } = data;
    if (email == "" || password == "" || last_name == "" || first_name == "") {
      toast.error("All fields are required");
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      toast.error("Please enter a valid email address");
      return;
    }
    setLoading(true)
    const res = await register_request(data);
    setLoading(false)

    if(res.status >= 400){
      toast.error(res.message)
      res?.errors?.email && setErrorEmail(res.errors.email[0])
      return
    }
    navigate("/verify?email="+email + "&type=active")
  };

  return (
    <form onSubmit= {handleRegister}className="wrap">
      <Navigation title="Sign up" />
      <div className="py-4">
        <h2 className="font-bold text-2xl">Sign up</h2>
        <p className="text-[14px]">
          If you don't have an account, please register here
        </p>

        <div className="md:grid block md:gap-4 md:grid-cols-2">
          <div className="flex flex-col gap-2">
            <h3>Last name</h3>
            <input
              type="text"
              placeholder="Last name"
              className="outline-none border border-gray-200 px-2 py-2"
              name="last_name"
              value={data.last_name}
              onChange={handleChange}
            />
          </div>

          <div className="flex flex-col gap-2">
            <h3>First name</h3>
            <input
              type="text"
              placeholder="First name"
              className="outline-none border border-gray-200 px-2 py-2"
              name="first_name"
              value={data.first_name}
              onChange={handleChange}
            />
          </div>

          <div className="flex flex-col gap-2">
            <h3>Email</h3>
            <input
              type="text"
              placeholder="Email"
              className="outline-none border border-gray-200 px-2 py-2"
              name="email"
              value={data.email}
              onChange={handleChange}
            />
            <p className="text-red-500 text-[12px]">{errorEmail}</p>

          </div>
          <div className="flex flex-col gap-2">
            <h3>Password</h3>
            <input
              type="password"
              placeholder="Password"
              className="outline-none border border-gray-200 px-2 py-2"
              name="password"
              value={data.password}
              onChange={handleChange}
            />
          </div>
        </div>
        <div className="flex items-center gap-4 mt-4">
          <button
            className="bg-black px-4 py-2 text-white hover:opacity-70"
            onClick={handleRegister}
            disabled = {loading}
          >
            Sign up{loading ? "..." : ""}
          </button>
          <Link to="/login">Sign in</Link>
        </div>
      </div>

      {loading && <Loading/>}
    </form>
  );
};

export default Register;
