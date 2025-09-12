// src/pages/Membership.jsx
import React, { useState } from "react";
import { useAuth } from "../../hooks/useAuth";
import { FormInput, FormButton, ErrorMessage } from "../../Components/Modal/Ui";

const Membership = () => {
  const { signup, error } = useAuth();
  const [formData, setFormData] = useState({
    email: "",
    username: "",
    password: "",
    confirmPassword: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const success = await signup(formData);
    if (success) {
      alert("회원가입 완료! 로그인 페이지로 이동합니다.");
      // 필요하면 navigate("/login");
    }
  };

  return (
    <div>
      <h1>회원가입</h1>
      <form onSubmit={handleSubmit}>
        <FormInput
          type="email"
          name="email"
          placeholder="이메일"
          value={formData.email}
          onChange={handleChange}
        />
        <FormInput
          type="text"
          name="username"
          placeholder="닉네임"
          value={formData.username}
          onChange={handleChange}
        />
        <FormInput
          type="password"
          name="password"
          placeholder="비밀번호"
          value={formData.password}
          onChange={handleChange}
        />
        <FormInput
          type="password"
          name="confirmPassword"
          placeholder="비밀번호 확인"
          value={formData.confirmPassword}
          onChange={handleChange}
        />
        <ErrorMessage error={error} />
        <FormButton>회원가입</FormButton>
      </form>
    </div>
  );
};

export default Membership;
