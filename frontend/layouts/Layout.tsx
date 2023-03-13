import React from 'react';
import { classNameModifiers } from 'utils/utils';

interface LayoutTypes {
  children: React.ReactNode;
  layout_prefix?: string;
  layout_modifier?: string;
}

const Layout: React.FC<LayoutTypes> = ({
  children,
  layout_prefix,
  layout_modifier,
}) => {
  return (
    <main
      className={[
        classNameModifiers(layout_prefix, layout_modifier, 'layout'),
      ].join(' ')}
    >
      {children}
    </main>
  );
};

export default Layout;
