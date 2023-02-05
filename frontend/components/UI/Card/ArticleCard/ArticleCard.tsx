import Image from 'next/image';
import React from 'react';
import { classNameModifiers } from 'utils/utils';
import Heading from '../../Heading/Heading';

interface ArticleCardTYpes {
  articleCard_prefix?: string;
  articleCard_modifier?: string;
  onClick?: React.MouseEventHandler;
  articleTitle: string;
  articleImage?: string;
  articleTags?: string[];
  active_tags?: string[];
}

const ArticleCard: React.FC<ArticleCardTYpes> = ({
  articleCard_prefix,
  articleCard_modifier,
  onClick,
  articleTitle,
  articleImage,
  articleTags,
  active_tags,
}) => {
  return (
    <div
      className={classNameModifiers(
        articleCard_prefix,
        articleCard_modifier,
        'article__card'
      )}
      onClick={onClick}
    >
      <div className="article-card-image__wrapper">
        {articleImage && (
          <Image
            src={articleImage}
            alt={articleTitle}
            fill
            className="article__image"
          />
        )}
      </div>
      <div className="article-card-content__warpper">
        <Heading
          heading_label={articleTitle}
          headingLevel="h5"
          heading_prefix="article-card"
        />
        <div className="article-card__tags">
          {articleTags &&
            articleTags.map((tag) => (
              <span
                className={[
                  'article-card__tag',
                  active_tags?.includes(tag) ? 'selected' : '',
                ].join(' ')}
              >
                {tag}
              </span>
            ))}
        </div>
      </div>
    </div>
  );
};

export default ArticleCard;
