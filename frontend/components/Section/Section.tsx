import React, { CSSProperties } from 'react';
import { classNameModifiers } from 'utils/utils';
import Heading from '../UI/Heading/Heading';

interface SectionTypes {
  children: React.ReactNode;
  section_prefix?: string;
  section_modifier?: string;
  section_heading_label?: string;
  section_heading_level?: string;
  section_heading_icon?: string;
  seection_style?: CSSProperties;
}

const Section: React.FC<SectionTypes> = ({
  children,
  section_prefix,
  section_modifier,
  section_heading_label,
  section_heading_level = 'h2',
  section_heading_icon,
  seection_style,
}) => {
  return (
    <section
      className={classNameModifiers(
        section_prefix,
        section_modifier,
        'section'
      )}
      style={seection_style}
    >
      {section_heading_label && (
        <Heading
          heading_label={section_heading_label}
          headingLevel={section_heading_level}
          heading_icon={section_heading_icon}
          heading_prefix="section"
        />
      )}
      <div className="section__content">{children}</div>
    </section>
  );
};

export default Section;
