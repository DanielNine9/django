import React, { useState } from "react";
import { toast } from "react-toastify";
import Loading from "../Loading";
import { verify_reset_password_request } from "../../api";
import { useNavigate } from "react-router-dom";

const init = {
  password: "",
  re_password: "",
};
const ResetPassword = () => {
  const [data, setData] = useState(init);
  const [loading, setLoading] = useState(false);
  const [getToken, setGetToken] = useState(false);
  const navigate = useNavigate();
  const searchParams = new URLSearchParams(window.location.search);
  const email = searchParams.get("email");
  const token = searchParams.get("token");

  const onChangeInput = (e) => {
    const { name, value } = e.target;
    setData({ ...data, [name]: value });
  };

  const handleChangePassword = async (e) => {
    e.preventDefault();
    const { password, re_password } = data;
    if (password == "" || re_password == "") {
      toast.error("All fields are required");
      return;
    }
    if (password != re_password) {
      toast.error("Password does not match password confirmation");
      return;
    }
    setLoading(true);
    const request_data = {
      email,
      token,
      password,
    };
    console.log(request_data)
    const res = await verify_reset_password_request(request_data);
    setLoading(false);
    console.log(res)
    if (res.status >= 400) {
      toast.error(res.message);
      if (res.message == "Token is expired") setGetToken(true);
      return;
    }

    navigate("/login");
  };

  return (
    <div>
      <div className="text-center text-2xl mt-4">
        <h2>Reset password</h2>
      </div>
      <form onSubmit={handleChangePassword} className="w-1/2 mx-auto my-4">
        <div className="flex flex-col gap-2">
          <h3>Password</h3>
          <input
            type="password"
            placeholder="Email"
            className="outline-none border border-gray-200 px-2 py-2"
            onChange={onChangeInput}
            value={data.password}
            name="password"
          />
        </div>

        <div className="flex flex-col gap-2">
          <h3>Confirm password</h3>
          <input
            type="password"
            placeholder="Confirm password"
            className="outline-none border border-gray-200 px-2 py-2"
            onChange={onChangeInput}
            value={data.re_password}
            name="re_password"
          />
        </div>

        <div
          onClick={handleChangePassword}
          className="flex items-center gap-4 mt-4"
        >
          <button className="bg-black px-4 py-2 text-whitehover:opacity-10 text-white">
            Change password
          </button>
        </div>
      </form>
      {loading && <Loading />}
    </div>
  );
};

export default ResetPassword;
