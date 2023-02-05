import React from 'react';
import { classNameModifiers } from 'utils/utils';

interface MainLayoutTypes {
  children: React.ReactNode;
  layout_prefix?: string;
  layout_modifier?: string;
}

function ass(num1: number, mun2: number) {
  return num1 + mun2;
}

const MainLayout: React.FC<MainLayoutTypes> = ({
  children,
  layout_prefix,
  layout_modifier,
}) => {
  return (
    <div
      className={[
        classNameModifiers(layout_prefix, layout_modifier, 'layout'),
      ].join(' ')}
    >
      {children}
    </div>
  );
};

export default MainLayout;
