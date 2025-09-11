import { useState, createContext, useContext } from "react";
import api from "../utils/api";
import { showSuccessAlert, showErrorAlert } from './../utils/alertUtiles';
import {useNavigate} from "react-router-dom";


const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [error, setError] = useState("");
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser]=useState(null);
  const navigate=useNavigate();


  const login = async (email, password) => {
    try{
      const response=await api.post("/users/login", {email, password});

      if(response.status===200){
        setUser(response.data);
        setIsAuthenticated(true);
        showSuccessAlert("로그인 성공");
        return true;
      }
    }
    catch(error){
      console.log(error);
      setIsAuthenticated(false);
      return false;
    }
  };

  const verifyJWTtoken=async() =>{

    try{
      const response=await api.get("users/userme");
      setIsAuthenticated(true);
      setUser(response.data); //현재 로그인한 사람 정보 세팅
      return true;

    }catch(error){
      if(error.response?.status===401){
        const detail = error.response.data?.detail;

        // if(detail===""){
            navigate("/login")
        // }
      }
    }

  }








  // const signup = async ({email, username, password, confirmPassword}) => {
  //   //유효성 검사
  //   setError("회원가입에 실패했습니다");
  //   return false;

  //   // try{
  //   //   const response=await api.post("/users/singup", {email, username, password});
  //   // }
  // };

  // const logout = async () => {
  //   const response=await api.post("/users/logout");
  //   alert("로그아웃");
  // };

  return (
    <AuthContext.Provider
      value={{ error, setError, isAuthenticated, login, signup, logout }}
    >
      {children}
    </AuthContext.Provider>
  );
};

// 🔹 Context를 안전하게 가져오기 위한 훅
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth는 반드시 <AuthProvider> 안에서 사용해야 합니다.");
  }
  return context;
};
