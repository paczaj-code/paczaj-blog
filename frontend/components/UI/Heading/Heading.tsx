import Icon from '@/components/Icon/Icon';
import React from 'react';
import { classNameModifiers } from 'utils/utils';

interface HeadingTypes extends React.HTMLAttributes<HTMLHeadingElement> {
  headingLevel: React.ElementType | string;
  heading_label: string;
  heading_icon?: string;
  heading_modifier?: string;
  heading_prefix?: string;
  heading_foretext?: string;
}

const Heading: React.FC<HeadingTypes> = ({
  headingLevel,
  heading_label,
  heading_icon,
  heading_prefix,
  heading_modifier,
}) => {
  const HeadingTag = headingLevel;

  return (
    <HeadingTag
      className={classNameModifiers(
        heading_prefix,
        heading_modifier,
        'heading'
      )}
    >
      {heading_icon && <Icon icon={heading_icon} />}
      <span>{heading_label}</span>
    </HeadingTag>
  );
};

export default Heading;
