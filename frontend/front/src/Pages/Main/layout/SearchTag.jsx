import React from "react";

const SearchTag = ({ search, onClear }) => {
  if (!search) return null;

  return (
    <div className="mb-4 flex items-center">
      <span className="text-gray-600 mr-2">검색 필터:</span>
      <div className="bg-purple-100 text-purple-800 px-3 py-1 rounded-full flex items-center">
        {search}
        <button
          onClick={onClear}
          className="ml-2 text-purple-600 hover:text-purple-800"
        >
          ✕
        </button>
      </div>
    </div>
  );
};

export default SearchTag;
