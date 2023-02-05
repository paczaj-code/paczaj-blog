import React from 'react';
import { classNameModifiers } from 'utils/utils';

interface DividerTypes {
  divider_prefix?: string;
  divider_modifier?: string;
}

const Divider: React.FC<DividerTypes> = ({
  divider_modifier,
  divider_prefix,
}) => {
  return (
    <hr
      className={classNameModifiers(
        divider_prefix,
        divider_modifier,
        'divider'
      )}
    />
  );
};

export default Divider;
