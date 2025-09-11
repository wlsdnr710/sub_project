import Swal from "sweetalert2";

export const handleAuthError = async (error) => {
  if (error.response?.status === 401) {
    await Swal.fire({
      title: "로그인이 필요!",
      text: "이 페이지를 이용하려면 로그인하세요.",
      icon: "warning",
      confirmButtonText: "확인",
      confirmButtonColor: "#34D399",
    });
    return true;
  }
  return false;
};

export const showErrorAlert = (
  error,
  defaultMessage = "오류가 발생."
) => {
  Swal.fire({
    icon: "error",
    title: "오류 발생",
    text:
      error.response?.data?.error ||
      error.response?.data?.detail ||
      defaultMessage,
    confirmButtonColor: "#EF4444",
  });
};

export const showSuccessAlert = (message) => {
  Swal.fire({
    icon: "success",
    title: "성공",
    text: message,
    confirmButtonColor: "#34D399",
  });
};

export const showConfirmDialog = async (
  title,
  text,
  confirmButtonText = "확인",
  cancelButtonText = "취소"
) => {
  return await Swal.fire({
    title,
    text,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#d33",
    cancelButtonColor: "#3085d6",
    confirmButtonText,
    cancelButtonText,
  });
};