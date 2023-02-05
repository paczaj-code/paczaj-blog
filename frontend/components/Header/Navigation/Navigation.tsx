import React, { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/router';
import SubMenu from './SubMenu';
import Heading from '@/components/UI/Heading/Heading';
import Icon from '@/components/Icon/Icon';

export interface MenuItemTypes {
  name: string;
  target?: string;
  icon?: string;
}

export interface MenuTypes extends MenuItemTypes {
  subMenu?: { name: string; icon?: string; subMenuItems: MenuItemTypes[] }[];
}

const Navigation = ({
  menuItems,
  showMenu,
  onClick,
}: {
  menuItems: MenuTypes[];
  showMenu: boolean;
  onClick: React.MouseEventHandler<HTMLElement>;
}) => {
  const [showSubMenu, setShowSubmenu] = useState<string | undefined>(undefined);
  const router = useRouter();

  return (
    <nav
      id="main__menu"
      className={showMenu ? 'show__menu' : ''}
      onClick={onClick}
    >
      <div className="mobile-menu__header">
        <Heading
          headingLevel="h2"
          heading_label="Menu"
          heading_prefix="mobile_title"
        />
        <Icon icon="icon-circle-left" icon_modifier="close-menu" />
      </div>
      <ul className="menu__list">
        <li className="menu__item">
          <Link
            href="/"
            className={
              router.asPath === '/' ? 'menu__link--active' : 'menu__link'
            }
          >
            Home
          </Link>
        </li>
        {menuItems.map((menuItem, index) => {
          const matcher = new RegExp(menuItem.target + '/', 'g');
          return (
            <li
              className="menu__item"
              key={index}
              onMouseOver={() => setShowSubmenu(menuItem.name)}
              onMouseLeave={() => setShowSubmenu(undefined)}
            >
              <>
                <Link
                  href={menuItem.target!}
                  className={
                    router.asPath === menuItem.target ||
                    matcher.test(router.asPath)
                      ? 'menu__link--active'
                      : 'menu__link'
                  }
                >
                  {menuItem.name}
                </Link>
                {menuItem.subMenu?.length && (
                  <SubMenu
                    subMenu={menuItem.subMenu}
                    prev_path={menuItem.target}
                    showSubmenu={showSubMenu}
                    subMenuName={menuItem.name}
                    setShowSubmenu={setShowSubmenu}
                  />
                )}
              </>
            </li>
          );
        })}
      </ul>
    </nav>
  );
};

export default Navigation;
