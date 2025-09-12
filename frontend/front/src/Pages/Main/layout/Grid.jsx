import React from "react";
import PostCard from "../PostCard";

const Grid = ({ posts, loading, onVote }) => {
  if (loading) {
    return <p className="text-center text-gray-500 col-span-4"></p>;
  }

  if (posts.length === 0) {
    return (
      <p className="text-center text-gray-500 col-span-4">
        등록된 게시글이 없습니다.
      </p>
    );
  }

  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 xl:grid-cols-4 gap-6">
      {posts.map((post, idx) => (
        <PostCard key={idx} post={post} onVote={onVote} />
      ))}
    </div>
  );
};

export default Grid;
