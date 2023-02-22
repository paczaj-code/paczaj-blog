import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import parse from 'html-react-parser';

// const articles = [
//   {
//     id: 4,
//     title: 'Pandas - biblioteka dla',
//     slug: 'pandas-biblioteka-dla',
//     category_slug: 'pandas',
//   },
//   {
//     id: 1,
//     title: 'Co to są relacyjne bazy danych?',
//     slug: 'co-to-sa-relacyjne-bazy-danych',
//     category_slug: 'sql',
//   },
//   {
//     id: 6,
//     title: 'Dipasss',
//     slug: 'dipasss',
//     category_slug: 'sql',
//   },
//   {
//     id: 2,
//     title: 'Jak pracować z bazą',
//     slug: 'jak-pracowac-z-baza',
//     category_slug: 'sql',
//   },
//   {
//     id: 5,
//     title: 'Instalacja bazy danych do ćwiczeń.',
//     slug: 'instalacja-bazy-danych-do-cwiczen',
//     category_slug: 'sql',
//   },
// ];

const ArticlesBySlug = ({ article }: any) => {
  // const router = useRouter();
  // const paths = articles.map((article: any) => {
  //   return {
  //     params: {
  //       category_slug: article.category_slug,
  //       article_slug: article.slug,
  //     },
  //   };
  // });

  // useEffect(() => {
  //   setPosts(article);
  // }, []);

  const [posts, setPosts] = useState<any>();
  const router = useRouter();
  // useEffect(() => {
  //   const handleComplete = () => {
  //     setPosts(article);
  //     // setActiveTags([]);
  //   };
  //   router.events.on('routeChangeComplete', handleComplete);
  //   router.events.on('routeChangeError', handleComplete);

  //   return () => {
  //     router.events.off('routeChangeComplete', handleComplete);
  //     router.events.off('routeChangeError', handleComplete);
  //   };
  // }, [router]);
  // console.log(posts);

  return (
    <div>
      {article && article.title}
      <article>{article && parse(article.content)}</article>

      {/* <article> {article.content && parse(article.content)}</article> */}
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
    fallback: true,
  };
}

export default ArticlesBySlug;
