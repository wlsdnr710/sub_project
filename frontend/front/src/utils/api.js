import axios from "axios";

//http요청 보내는 라이브러리
const api=axios.create({
    baseURL: import.meta.env.VITE_API_URL,
    withCredentials:true,
});


export default api;