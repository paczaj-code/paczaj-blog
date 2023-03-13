import React from 'react';
import Head from 'next/head';
import parse from 'html-react-parser';
import { useRouter } from 'next/router';
import Section from '@/components/Section/Section';
import ItemCard from '@/components/UI/Card/ItemCard';
import Icon from '@/components/Icon/Icon';
import Heading from '@/components/UI/Heading/Heading';
import Layout from 'layouts/Layout';
interface CategoryTypes {
  id: number;
  name: string;
  slug: string;
  posts: number;
  description?: string;
  subcount: number;
  icon: string;
  sub_categories: CategoryTypes[];
}

interface CategoriesTypes {
  categories: CategoryTypes[];
}

const Articles: React.FC<CategoriesTypes> = ({ categories }) => {
  const router = useRouter();
  return (
    <>
      <Head>
        <title>Blog</title>
      </Head>
      <Layout layout_modifier="full">
        {categories &&
          categories.map((category, index) => (
            <Section key={category.id} section_prefix="category">
              <div className="category__description">
                <Heading headingLevel="h2" heading_label={category.name} />
                <div>{parse(category.description!)}</div>
              </div>
              {/* </div> */}
              <div className="category__cards">
                {category.sub_categories.length &&
                  category.sub_categories.map((subcategory, index) => (
                    <ItemCard
                      key={index}
                      itemCard_prefix="category"
                      // itemCard_modifier={subcategory.slug}
                      onClick={() => router.push(`/blog/${subcategory.slug}`)}
                    >
                      {subcategory.icon && (
                        <Icon icon_prefix="item-card" icon={subcategory.icon} />
                      )}
                      <h3>{subcategory.name}</h3>
                    </ItemCard>
                  ))}
              </div>
            </Section>
          ))}
      </Layout>
    </>
  );
};

const fetchCategories = async () => {
  const response = await fetch(process.env.API + 'category/');
  return response;
};
export async function getStaticProps({ props }: any) {
  let categories;

  try {
    const res = await fetchCategories();
    categories = await res.json();

    if (res.status === 404) {
      return { notFound: true };
    }
    return {
      props: {
        categories,
      },
      revalidate: 60,
    };
  } catch (error) {
    console.log('There was an error', error);
    return { notFound: true };
  }
}

export default Articles;
