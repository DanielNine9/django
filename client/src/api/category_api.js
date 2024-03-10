import axios from "./axios.js";

export const get_categories_request =async () => {
    try {
        const res = await axios.get("category/")
        return res
    } catch (err) {
        return err.response.data
    }
}