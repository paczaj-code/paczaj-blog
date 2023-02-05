import React, { Dispatch, SetStateAction, useEffect } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/router';
import { MenuItemTypes } from './Navigation';

interface SubMenuTypes {
  subMenu?: { name: string; icon?: string; subMenuItems: MenuItemTypes[] }[];
  prev_path?: string;
  showSubmenu: string | undefined;
  subMenuName: string;
  setShowSubmenu: Dispatch<SetStateAction<string | undefined>>;
}

const SubMenu = ({
  subMenu,
  prev_path,
  showSubmenu,
  subMenuName,
  setShowSubmenu,
}: SubMenuTypes) => {
  const router = useRouter();
  useEffect(() => {
    const handleRouteChange = (url: any, { shallow }: any) => {
      setShowSubmenu(undefined);
    };

    router.events.on('routeChangeStart', handleRouteChange);
    return () => {
      router.events.off('routeChangeStart', handleRouteChange);
    };
  }, []);
  return (
    <div
      className={[
        'submenu__wrapper',
        showSubmenu === subMenuName ? 'show' : '',
      ].join(' ')}
    >
      <div className="submenu__content show">
        {subMenu?.length &&
          subMenu.map((subItems, index) => (
            <div className="subitems__wrapper" key={index}>
              <p className="subitems__title">
                <i className={subItems.icon}></i>
                <span>{subItems.name}</span>
              </p>
              <ul>
                {subItems.subMenuItems.map((subItem, index) => {
                  const matcher = new RegExp(
                    `${prev_path}${subItem.target}`,
                    'g'
                  );

                  return (
                    <li key={index} className="submenu__item">
                      <Link
                        href={`${prev_path}${subItem.target}`}
                        className={
                          matcher.test(router.asPath)
                            ? 'submenu__link--active'
                            : 'submenu__link'
                        }
                      >
                        <i className={subItem.icon}></i>
                        {subItem.name}
                      </Link>
                    </li>
                  );
                })}
              </ul>
            </div>
          ))}
      </div>
    </div>
  );
};

export default SubMenu;
