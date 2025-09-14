import { useState } from "react";
import api from "../utils/api";
import {
  showErrorAlert,
  showSuccessAlert,
  handleAuthError,
} from "../utils/alertUtils";

export const usePost = () => {
  const [loading, setLoading] = useState(false);

  const fetchposts = async ({ sort, limit, offset, category, search }) => {
    setLoading(true);
    try {
      const params = {
        sort,
        limit,
        offset: offset - 1,
        category,
        ...(search && { search }),
      };
      const response = await api.get("/posts",{
        params,
      });

      if (response.status === 200) {
        return response.data;
      }
      return null;
    } catch (error) {
      //showErrorAlert(error, "게시글을 불러올 수 없습니다.");
      return null;
    } finally {
      setLoading(false);
    }
  };

  const countAllposts = async (category, search) => {
    setLoading(true);
    try {
      const params = {
        category,
        ...(search && { search }),
      };
      const response = await api.get("/posts/count", {
        params,
      });

      if (response.status === 200) {
        return response.data;
      }
      return null;
    } catch (error) {
      // showErrorAlert(error, "게시글을 불러올 수 없습니다.");
      return null;
    } finally {
      setLoading(false);
    }
  };

  const addpost = async (postData) => {
    setLoading(true);
    try {
      const response = await api.post("/posts", postData);

      if (response.status === 200) {
        showSuccessAlert("게시글이 성공적으로 생성되었습니다.");
        return response.data;
      }
      return null;
    } catch (error) {
      if (await handleAuthError(error)) return null;
      showErrorAlert(error, "게시글을 생성할 수 없습니다.");
      return null;
    } finally {
      setLoading(false);
    }
  };

  const getpostById = async (postId) => {
    setLoading(true);
    try {
      const response = await api.get(`/posts/${postId}`);

      if (response.status === 200) {
        return response.data;
      }
      return null;
    } catch (error) {
      //showErrorAlert(error, "게시글을 불러올 수 없습니다.");
      return null;
    } finally {
      setLoading(false);
    }
  };

  return {
    loading,
    fetchposts,
    countAllposts,
    addpost,
    getpostById,
  };
};
