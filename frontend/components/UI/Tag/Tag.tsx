import React from 'react';
import { classNameModifiers } from 'utils/utils';

interface TagTypes {
  name: string;
  slug: string;
  onClick?: React.MouseEventHandler;
  tag_prefix?: string;
  tag_modifier?: string;
  isActive?: boolean;
}

const Tag: React.FC<TagTypes> = ({
  name,
  slug,
  onClick,
  tag_prefix,
  tag_modifier,
  isActive = false,
}) => {
  tag_modifier = isActive ? 'active' : '';
  return (
    <span
      className={classNameModifiers(tag_prefix, tag_modifier, 'tag')}
      onClick={onClick}
      data-tagname={slug}
      data-testid="tag"
    >
      {name}
    </span>
  );
};

export default Tag;
