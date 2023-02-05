import React from 'react';
import { useRouter } from 'next/router';
import logo from '../../../public/images/logo.png';
import Image from 'next/image';

interface LogoTypes {
  onClick?: React.MouseEventHandler;
}

const Logo: React.FC<LogoTypes> = ({ onClick }) => {
  const router = useRouter();
  return (
    <div className="logo__wrapper" onClick={() => router.push('/')}>
      <Image src={logo} alt="eyes" height={77} />
      <h1 className="logo">paczaj</h1>
    </div>
  );
};

export default Logo;
