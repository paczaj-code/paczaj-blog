import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import ArticleCard from '@/components/UI/Card/ArticleCard/ArticleCard';
import Heading from '@/components/UI/Heading/Heading';
import Divider from '@/components/UI/Divider/Divider';
import Tag from '@/components/UI/Tag/Tag';

const ArticlesByCategory = ({ articles }: any) => {
  const [posts, setPosts] = useState([]);
  const [activeTags, setActiveTags] = useState<string[]>([]);
  const router = useRouter();
  const handleTagsToggle = (tagName: string) => {
    !activeTags.includes(tagName)
      ? setActiveTags([...activeTags, tagName])
      : setActiveTags(activeTags.filter((i) => i !== tagName));
  };

  useEffect(() => {
    const handleComplete = () => {
      setPosts(articles.posts);
      setActiveTags([]);
    };
    router.events.on('routeChangeComplete', handleComplete);
    router.events.on('routeChangeError', handleComplete);

    return () => {
      router.events.off('routeChangeComplete', handleComplete);
      router.events.off('routeChangeError', handleComplete);
    };
  }, [router]);

  useEffect(() => {
    if (activeTags.length) {
      setPosts(
        articles.posts.filter((element: any) =>
          element.article_tags.some((f: any) => activeTags.includes(f))
        )
      );
    } else {
      setPosts(articles.posts);
    }
  }, [activeTags]);

  return (
    <>
      <Heading
        headingLevel="h2"
        heading_label={articles.category.name}
        heading_icon={articles.category.icon}
        heading_prefix="article-category"
      />
      <Divider divider_prefix="carticle-category" />
      <div className="articles__wrapper">
        <div className="articles-cards__wrapper">
          {posts.map((article: any) => (
            <ArticleCard
              articleTitle={article.title}
              key={article.id}
              articleImage={article.image_url && article.image_url}
              articleTags={article.article_tags}
              onClick={() => router.push(`${router.asPath}/${article.slug}`)}
              active_tags={activeTags}
            />
          ))}
        </div>
        <div className="articles-tags__wrapper">
          <Heading
            headingLevel="h5"
            heading_label="Filtruj"
            heading_prefix="articles-tags"
          />
          {articles.tags.map(
            (tag: any, index: React.Key | null | undefined) => (
              <Tag
                key={index}
                name={tag}
                slug={tag}
                isActive={activeTags.includes(tag)}
                onClick={() => handleTagsToggle(tag)}
              />
            )
          )}
        </div>
      </div>
    </>
  );
};

export async function getStaticProps(context: any) {
  const { params } = context;
  let articles;

  try {
    const response = await fetch(
      process.env.API + `posts/${params['category_slug']}`
    );

    articles = await response.json();

    if (response.status === 404) {
      return { notFound: true };
    }
    return {
      props: {
        articles,
      },
      revalidate: 30,
    };
  } catch (error) {
    console.log('There was an error', error);
    return { notFound: true };
  }
}

export async function getStaticPaths() {
  const res = await fetch(process.env.API + 'category/');
  const response = await res.json();

  const paths = response
    .map((item: any) =>
      item.sub_categories.map((sub_item: any) => ({
        params: { category_slug: sub_item.slug },
      }))
    )
    .flat();

  return {
    paths,
    fallback: false,
  };
}

export default ArticlesByCategory;
