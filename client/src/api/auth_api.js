import axios from "./axios.js";

export const register_request =async (data) => {
    try {
        const res = await axios.post("auth/register/", data)
        return res
    } catch (err) {
        // dispatch(loginFailed())
        return err.response.data
    }
}
export const login_request =async (data) => {
    try {
        const res = await axios.post("auth/login/", data)
        return res
    } catch (err) {
        return err.response.data
    }
}


export const active_account_request =async (email, token) => {
    const data = {
        "email": email,
        "token": token
    }
    try {
        const res = await axios.post("auth/active/", data)
        return res
    } catch (err) {
        return err.response.data
    }
}


export const reset_password_request =async (email, otp) => {
    try {
        const res = await axios.get("auth/reset?email="+email)
        return res
    } catch (err) {
        return err.response.data
    }
}

export const verify_reset_password_request =async (data) => {
    console.log("auth/reset?email="+data.email+"&token="+data.token)
    try {
        const res = await axios.post("auth/reset?email="+data.email+"&token="+data.token, {"password": data.password})
        // const res = await axios.post("auth/reset?email=dinhhuyfpt09@gmail.com&token=23")
        return res
    } catch (err) {
        return err.response.data
    }
}
