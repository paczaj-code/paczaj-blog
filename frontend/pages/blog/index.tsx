import React from 'react';
import { useRouter } from 'next/router';

import MainLayout from 'layouts/MainLayout';
import Section from '@/components/Section/Section';
import ItemCard from '@/components/UI/Card/ItemCard';
import Icon from '@/components/Icon/Icon';
import Button from '@/components/UI/Button/Button';
import db from '../../utils/db.json';
import Image from 'next/image';
import Heading from '@/components/UI/Heading/Heading';
import { useFetch } from 'hooks/useFetch';

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
    <MainLayout layout_prefix="blog">
      {categories &&
        categories.map((category, index) => (
          // <span></span>

          <Section
            key={category.id}
            section_prefix="category"
            section_modifier={category.slug}
            section_extra_classes={['fade-in-top']}
            // section_heading_label={category.name}
            // section_heading_icon={category.icon}
            // style={{animationDelay:}}
            seection_style={{ animationDelay: `${50 * index}ms` }}
          >
            {/* <Image
            // loader={myLoader}
            src={require('../../public/images/557-2.jpg')}
            alt="Picture of the author"
            width={500}
            height={500}
          /> */}
            <div className="section__wrapper">
              <div className={`section__image--${category.slug}`}></div>
              <div className="section__description">
                <Heading headingLevel="h3" heading_label={category.name} />
                <p>{category.description}</p>
              </div>
            </div>

            {/* <Heading
            headingLevel="h1"
            heading_label={category.name}
            heading_prefix="category"
            heading_icon={category.icon ? category.icon : undefined}
          /> */}
            {/* <div
            className="category__description"
            dangerouslySetInnerHTML={{ __html: category.description! }}
          ></div> */}
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
    </MainLayout>
  );
};

export async function getStaticProps({ props }: any) {
  let categories;

  try {
    const response = await fetch(process.env.API + 'category/');
    // console.log(response.status);

    categories = await response.json();

    if (response.status === 404) {
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
