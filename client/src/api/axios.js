import axios from "axios";

const instance = axios.create({
    // baseURL: 'http://localhost:3000/',
    
    // baseURL: 'https://car-manager-backend-ai3i.onrender.com/',
    baseURL: 'http://localhost:8000/api/',

});

export default instance