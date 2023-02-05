import React, { useState, useEffect } from 'react';
import Navigation from './Navigation/Navigation';
import Logo from './Logo/Logo';
import { menuItems } from 'utils/menuItems';
import useScrollDirection from 'hooks/useScrollDirection';

const Header = () => {
  const [isMenuVisible, setIsMenuVisible] = useState<boolean>(false);

  const scrollDirection = useScrollDirection();

  return (
    <header
      className={`app__header app__header--${
        scrollDirection === 'up' || null ? 'show' : 'hide'
      }`}
    >
      <div className="header__content">
        <button
          onClick={() => setIsMenuVisible(!isMenuVisible)}
          className="menu__toggler"
        >
          <i className="icon-th-menu-outline"></i>
        </button>
        <Logo />
        <Navigation
          menuItems={menuItems}
          showMenu={isMenuVisible}
          onClick={() => setIsMenuVisible(!isMenuVisible)}
        />
      </div>
    </header>
  );
};

export default Header;
