import axios from "./axios.js";

export const get_products_request =async () => {
    try {
        const res = await axios.get("product/")
        return res
    } catch (err) {
        return err.response.data
    }
}