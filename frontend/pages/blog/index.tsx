import React from 'react';
import parse from 'html-react-parser';
import { useRouter } from 'next/router';
import Section from '@/components/Section/Section';
import ItemCard from '@/components/UI/Card/ItemCard';
import Icon from '@/components/Icon/Icon';
import Button from '@/components/UI/Button/Button';
import Heading from '@/components/UI/Heading/Heading';

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
      {categories &&
        categories.map((category, index) => (
          <Section
            key={category.id}
            section_prefix="category"
            section_modifier={category.slug}
            section_extra_classes={['fade-in-top']}
            seection_style={{ animationDelay: `${50 * index}ms` }}
          >
            <div className="section__wrapper">
              <div className={`section__image--${category.slug}`}></div>
              <div className="section__description">
                <Heading headingLevel="h3" heading_label={category.name} />
                <div>{parse(category.description!)}</div>
              </div>
            </div>
            {category.sub_categories.length &&
              category.sub_categories.map((subcategory, index) => (
                <ItemCard
                  key={index}
                  itemCard_prefix="category"
                  itemCard_modifier={subcategory.slug}
                  onClick={() => router.push(`/blog/${subcategory.slug}`)}
                >
                  {subcategory.icon && (
                    <Icon icon_prefix="item-card" icon={subcategory.icon} />
                  )}
                  <h3>{subcategory.name}</h3>
                  <Button button_type="button" button_prefix="item-card">
                    <span className="item-card__button__text">paczaj</span>
                    <Icon
                      icon="icon-circle-right"
                      icon_prefix="item-card__button"
                    />
                  </Button>
                </ItemCard>
              ))}
          </Section>
        ))}
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
