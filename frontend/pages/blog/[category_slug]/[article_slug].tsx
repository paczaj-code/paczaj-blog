import React, { useState, useEffect } from 'react';
// import { useRouter } from 'next/router';
import parse from 'html-react-parser';

import * as Prism from 'prismjs';
import 'prismjs/components/prism-sql.js';
import 'prismjs/components/prism-python.js';
import 'prismjs/plugins/line-numbers/prism-line-numbers';
import 'prismjs/plugins/toolbar/prism-toolbar';
import 'prismjs/plugins/toolbar/prism-toolbar.css';

import 'prismjs/plugins/copy-to-clipboard/prism-copy-to-clipboard';
import 'prismjs/plugins/line-numbers/prism-line-numbers.css';

const ArticlesBySlug = ({ article }: any) => {
  const [hasMounted, setHasMounted] = useState(false);

  useEffect(() => setHasMounted(true), []);

  useEffect(() => {
    const highlight = async () => {
      Prism.highlightAll();
    };

    highlight();
  }, [hasMounted]);

  return (
    <div>
      {article && article.title}
      <article>{hasMounted && parse(article.content)}</article>
    </div>
  );
};

export async function getStaticProps(context: any) {
  const { params } = context;
  let article;

  try {
    const response = await fetch(
      process.env.API + `post/${params['article_slug']}`
    );

    article = await response.json();

    if (response.status === 404) {
      return { notFound: true };
    }
    return {
      props: {
        article,
      },
      revalidate: 30,
    };
  } catch (error) {
    console.log('There was an error', error);
    return { notFound: true };
  }
}

export async function getStaticPaths() {
  const res = await fetch(process.env.API + 'posts/');
  const response = await res.json();
  // console.log(articles);
  //creating an array of objects
  const paths = response.map((article: any) => {
    return {
      params: {
        category_slug: article.category_slug,
        article_slug: article.slug,
      },
    };
  });
  // console.log(paths);
  return {
    paths,
    fallback: 'blocking',
  };
}

export default ArticlesBySlug;
