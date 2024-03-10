import React, { useState } from "react";
import Navigation from "../main/Navigation";
import { Link, useNavigate } from "react-router-dom";
import { login_request, reset_password_request } from "../../api/index";
import { toast } from "react-toastify";
import Loading from "../Loading";
import { useDispatch } from "react-redux";
import { storeUser } from "../../redux/authSlice";

const loginInit = {
  email: "",
  password: "",
};

const Login = () => {
  const [login, setLogin] = useState(loginInit);
  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const onChangeInput = (e) => {
    const { name, value } = e.target;
    setLogin({ ...login, [name]: value });
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    const { email, password } = login;
    if (email == "" || password == "") {
      toast.error("All fields are required");
      return;
    }
    console.log(login);
    setLoading(true);
    const res = await login_request(login);
    setLoading(false);
    if (res.status >= 400) {
      toast.error(res.message);
      return;
    }
    dispatch(storeUser(res.data.data[0]));
    navigate("/");
  };

  const handleResetPassword = async (e) => {
    e.preventDefault();
    if (email == "") return toast.error("Please enter a valid email address");
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      toast.error("Please enter a valid email address");
      return;
    }
    setLoading(true);
    const res = await reset_password_request(email);
    setLoading(false);
    if (res.status >= 400) {
      toast.error(res.message);
      return;
    }
    toast.success(res.data.message);
    navigate("/verify?email=" + email + "&type=");
  };

  return (
    <div className="wrap">
      <Navigation title="Sign in" />
      <div className="py-4">
        <h2 className="font-bold text-2xl">Sign in</h2>
        <p className="text-[14px]">
          If you already have an account, log in here.
        </p>

        <div className="md:flex block md:gap-4 md:justify-centeR">
          <form onSubmit={handleLogin} className="w-full">
            <div className="flex flex-col gap-2">
              <h3>Email</h3>
              <input
                type="text"
                placeholder="Email"
                className="outline-none border border-gray-200 px-2 py-2"
                onChange={onChangeInput}
                value={login.email}
                name="email"
              />
            </div>

            <div className="flex flex-col gap-2">
              <h3>Password</h3>
              <input
                type="password"
                placeholder="Password"
                className="outline-none border border-gray-200 px-2 py-2"
                onChange={onChangeInput}
                value={login.password}
                name="password"
              />
            </div>

            <div onClick={handleLogin} className="flex items-center gap-4 mt-4">
              <button className="bg-black px-4 py-2 text-whitehover:opacity-10 text-white">
                Sign in
              </button>
              <Link to="/register">Sign up</Link>
            </div>
          </form>

          <form onSubmit={handleResetPassword} className="w-full md:mt-[-20px]">
            <p className="text-[14px]">
              Forgot your password? Enter your email address to retrieve your
              password via email
            </p>

            <div className="flex flex-col gap-2">
              <h3>Email</h3>
              <input
                type="text"
                placeholder="Email"
                className="outline-none border border-gray-200 px-2 py-2"
                onChange={(e) => setEmail(e.target.value)}
                value={email}
              />
            </div>

            <button
              onClick={handleResetPassword}
              className="bg-black px-4 py-2 text-white mt-8"
            >
              Password retrieval
            </button>
          </form>
        </div>
      </div>
      {loading && <Loading />}
    </div>
  );
};

export default Login;
