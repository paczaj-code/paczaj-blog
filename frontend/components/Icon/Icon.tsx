import React from 'react';
import { classNameModifiers } from 'utils/utils';

interface IconTypes {
  icon: string;
  icon_modifier?: string;
  icon_prefix?: string;
}

const Icon: React.FC<IconTypes> = ({ icon, icon_modifier, icon_prefix }) => {
  return (
    <i
      className={[
        classNameModifiers(icon_prefix, icon_modifier, 'icon'),
        icon,
      ].join(' ')}
    ></i>
  );
};

export default Icon;
