import React from "react";
import { FaHeart } from "react-icons/fa";

const LikeInfo = ({ createdAt, likeCount }) => {
  return (
    <div className="mt-auto pt-4 flex justify-between items-center text-xs text-gray-400 border-t border-gray-300">
      <span>{createdAt}</span>
      <div className="flex items-center gap-2">
        <span className="flex items-center gap-1">
          <FaHeart />
          {likeCount}
        </span>
      </div>
    </div>
  );
};

export default LikeInfo;
