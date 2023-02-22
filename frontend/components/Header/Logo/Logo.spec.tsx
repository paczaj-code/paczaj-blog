import { render, screen } from '@testing-library/react';
import Logo from './Logo';

jest.mock('next/router', () => require('next-router-mock'));

describe('Test for Logo component', () => {
  it('renders a heading', () => {
    render(<Logo />);
    const logo = document.querySelector('.logo');
    expect(logo).toBeInTheDocument();
  });
});
