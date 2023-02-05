import React from 'react';
import { useRouter } from 'next/router';

const ArticlesBySlug = () => {
  const router = useRouter();
  //   console.log(router.query['article-slug']);

  return <div>{router.query['article-slug']}</div>;
};

export default ArticlesBySlug;
