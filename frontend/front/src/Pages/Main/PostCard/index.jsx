import React, { memo, useMemo } from "react";
import { Link } from "react-router-dom";
import VoteInfo from "./LikeInfo";

const PostCard = ({ post, onVote }) => {
  const formattedDate = useMemo(() => {
    return new Date(post.created_at).toLocaleString("ko-KR", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
    });
  }, [post.created_at]);

  return (
    // <Link to={`/post/${post.post_id}`}>
    <div
      className={`relative flex flex-col p-4 h-full border-2 rounded-lg transition-shadow hover:shadow-lg ${
        post.has_voted ? "bg-gray-100" : "bg-white"
      }`}
    >
      {post.has_voted && (
        <div className="absolute inset-0 z-10 flex items-center justify-center bg-white/70 rounded-lg">
          <span className="px-6 py-4 text-xl font-bold text-white bg-purple-500 rounded-lg">
            이미 클릭한 글입니다
          </span>
        </div>
      )}

      <div className="flex-1 flex flex-col">
        <div className="mb-2 flex justify-between items-start">
          <h3 className="text-xl font-semibold text-purple-600 line-clamp-2">
            {post.title}
          </h3>
          {post.category && (
            <span className="px-2 py-1 text-xs font-medium bg-purple-100 text-purple-800 rounded-full">
              {post.category}
            </span>
          )}
        </div>
        <p className="mb-4 text-sm text-gray-500 line-clamp-2">
          {post.description}
        </p>
        <VoteInfo createdAt={formattedDate} likeCount={post.like_count} />
      </div>
    </div>
    //  </Link>
  );
};

export default memo(PostCard);
