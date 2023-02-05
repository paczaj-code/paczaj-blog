import React from 'react';
import { classNameModifiers } from 'utils/utils';

interface TagTypes {
  name: string;
  slug: string;
  onClick?: React.MouseEventHandler;
  tag_prefix?: string;
  tag_modifier?: string;
  isActive: boolean;
  extra_class?: string;
}

const Tag: React.FC<TagTypes> = ({
  name,
  slug,
  onClick,
  tag_prefix,
  tag_modifier,
  isActive = false,
  extra_class,
}) => {
  tag_modifier = isActive ? 'active' : '';
  return (
    <span
      className={[
        classNameModifiers(tag_prefix, tag_modifier, 'tag'),
        extra_class,
      ].join(' ')}
      onClick={onClick}
      data-tagname={slug}
    >
      {name}
    </span>
  );
};

export default Tag;
