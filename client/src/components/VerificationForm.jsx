import React, { useState } from "react";
import AuthCode from "react-auth-code-input";
import {
  active_account_request,
  verify_reset_password_request,
} from "../api/index";
import { toast } from "react-toastify";
import { useNavigate, useSearchParams } from "react-router-dom";
import Loading from "./Loading";

const VerificationForm = () => {
  const [result, setResult] = useState();
  const searchParams = new URLSearchParams(window.location.search);
  const email = searchParams.get("email");
  const type = searchParams.get("type");
  const [getToken, setGetToken] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const [password, setPassword] = useState("");
  const active = type == "active";

  const handleOnChange = (res) => {
    setResult(res);
  };

  const handleSubmit = async (e) => {
    var res;

    setLoading(true);
    if (active) {
      res = await active_account_request(email, result);
    } else {
      res = await verify_reset_password_request({email, result});
    }
    setLoading(false);
    console.log(res);
    if (res.status >= 400) {
      toast.error(res.message);
      if (res.message == "Token is expired") setGetToken(true);
      return;
    }

    navigate("/login");
  };

  return (
    <div className="text-center w-2/5 mx-auto">
      <h2 className="text-4xl my-2">Verify code</h2>
      <AuthCode
        inputClassName="p-4 w-14 border mx-2 text-center"
        allowedCharacters="numeric"
        onChange={handleOnChange}
      />
      
      <div className="flex gap-4 justify-center">
        <button
          onClick={handleSubmit}
          className="bg-black px-4 py-2 text-whitehover:opacity-10 text-white mb-20 mt-4"
        >
          Send {active ? "activation code" : "reset password code"}
        </button>
        {getToken && (
          <button
            onClick={handleSubmit}
            className="bg-blue-400 px-4 py-2 text-whitehover:opacity-10 text-white mb-20 mt-4"
          >
            Send {active ? "active" : "reset password"} code again
          </button>
        )}
      </div>

      {loading && <Loading />}
    </div>
  );
};

export default VerificationForm;
