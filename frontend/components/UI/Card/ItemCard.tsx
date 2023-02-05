import React from 'react';
import { classNameModifiers } from 'utils/utils';

interface ItemCardTypes {
  children: React.ReactNode;
  itemCard_prefix?: string;
  itemCard_modifier?: string;
  onClick?: React.MouseEventHandler;
}

const ItemCard: React.FC<ItemCardTypes> = ({
  children,
  itemCard_modifier,
  itemCard_prefix,
  onClick,
}) => {
  return (
    <div
      className={classNameModifiers(
        itemCard_prefix,
        itemCard_modifier,
        'item-card'
      )}
      onClick={onClick}
    >
      {children}
    </div>
  );
};

export default ItemCard;
