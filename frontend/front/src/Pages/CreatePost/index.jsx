import React, { useState, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import { usePost } from "../../hooks/usePost";
import Swal from "sweetalert2";
import { CATEGORIES } from "../../constants/categories";
import FormField from "./layout/FormField";
import CategorySelect from "./layout/CategorySelect";
import SubmitButton from "./layout/SubmitButton";

const Createpost = () => {
  const { addpost } = usePost();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    title: "",
    desc: "",
    category: "",
  });

  const onChange = useCallback((e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  }, []);

  const onSubmit = useCallback(
    async (e) => {
      e.preventDefault();

      try {
        const result = await addpost(formData);
        if (result?.post_id) {
          Swal.fire({
            icon: "success",
            title: "게시글 생성 완료",
            text: "게시글이 성공적으로 생성되었습니다.",
            confirmButtonColor: "#10B981",
          });
          navigate(`/`);
        }
      } catch (error) {
        console.error("Error creating post:", error);
        Swal.fire({
          icon: "error",
          title: "게시글 생성 실패",
          text: "다시 시도해주세요.",
          confirmButtonColor: "#EF4444",
        });
      }
    },
    [formData, addpost, navigate]
  );

  return (
    <div className="flex items-center justify-center px-4">
      <div className="max-w-3xl w-full bg-white p-8 rounded-2xl shadow-xl">
        <h2 className="text-2xl font-bold text-gray-900 mb-6">
          새로운 글 생성
        </h2>
        <form onSubmit={onSubmit} className="space-y-6">
          <FormField
            label="제목"
            name="title"
            value={formData.title}
            onChange={onChange}
            placeholder="게시글 제목을 입력하세요"
          />
          <FormField
            label="설명"
            name="description"
            value={formData.description}
            onChange={onChange}
            placeholder="게시글에 대한 설명을 입력하세요"
          />
          <CategorySelect
            categories={CATEGORIES}
            value={formData.category}
            onChange={onChange}
          />
          <SubmitButton label="글 생성하기" />
        </form>
      </div>
    </div>
  );
};

export default Createpost;
