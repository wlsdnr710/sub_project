import React, { useEffect, useMemo, useCallback, useState } from "react";
import { useSearchParams } from "react-router-dom";
import Header from "./layout/Header";
import SearchTag from "./layout/SearchTag";
import Grid from "./layout/Grid";
import Pagination from "./layout/Pagination";
import { usePost } from "../../hooks/usePost";

const Main = () => {
  const { loading, fetchposts } = usePost();
  const [posts, setposts] = useState([]);
  const [totalposts, setTotalposts] = useState(0);

  const [searchParams, setSearchParams] = useSearchParams();

  const category = searchParams.get("category") || "";
  const sort = searchParams.get("sort") || "created_at";
  const search = searchParams.get("search") || "";
  const page = parseInt(searchParams.get("page") || "1", 10);
  const postsPerPage = 12;

  const loadposts = useCallback(async () => {
    const { posts, total } = await fetchposts({
      offset: page,
      limit: postsPerPage,
      sort,
      category,
      search,
    });
    setposts(posts);
    setTotalposts(total);
  }, [fetchposts, page, sort, category, search]);

  useEffect(() => {
    loadposts();
  }, [category, sort, page, search]);

  const onPageChange = (p) => {
    const updated = new URLSearchParams(searchParams);
    updated.set("page", p);
    setSearchParams(updated);
  };

  const onSortChange = (e) => {
    const updated = new URLSearchParams(searchParams);
    updated.set("sort", e.target.value);
    updated.set("page", 1);
    setSearchParams(updated);
  };

  const onSeachClear = () => {
    const updated = new URLSearchParams(searchParams);
    updated.delete("search");
    setSearchParams(updated);
  };
  const onVote = (post_id, index) => {
    console.log(post_id, index);
  };

  const titleText = useMemo(() => {
    if (search) return `"${search}" 검색 결과`;
    if (category) return `${category} 게시글`;
    return "전체 게시글";
  }, [search, category]);

  return (
    <div className="w-full px-4 py-4 bg-white">
      <div className="max-w-8xl mx-auto">
        <Header
          title={titleText}
          total={totalposts}
          sort={sort}
          onSortChange={onSortChange}
        />
        <SearchTag search={search} onClear={onSeachClear} />
        <Grid posts={posts} loading={loading} onVote={onVote} />
        <Pagination
          currentPage={page}
          total={totalposts}
          perPage={postsPerPage}
          onPageChange={onPageChange}
        />
      </div>
    </div>
  );
};

export default Main;
