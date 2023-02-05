import React from 'react';
import Icon from '@/components/Icon/Icon';
import { classNameModifiers } from 'utils/utils';

interface ButtonTypes {
  children: React.ReactNode;
  button_type: 'button' | 'submit' | 'reset';
  button_modifier?: string;
  button_prefix?: string;
  onClick?: React.MouseEventHandler;
}

const Button: React.FC<ButtonTypes> = ({
  children,
  button_type,
  button_modifier,
  button_prefix,
  onClick,
}) => {
  return (
    <button
      type={button_type}
      className={classNameModifiers(button_prefix, button_modifier, 'button')}
      onClick={onClick}
    >
      {children}
    </button>
  );
};

export default Button;
