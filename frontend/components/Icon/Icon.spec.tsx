import { render } from '@testing-library/react';
import Icon from './Icon';

describe('Tests for Icon component', () => {
  it('should be icon class without prefix and modifier', () => {
    render(<Icon icon="icon-moon" />);
    const icon = document.querySelector('.icon-moon');
    expect(icon).toBeInTheDocument();
  });
  it('should be "prefix__icon" class with prefix "prefix"', () => {
    render(<Icon icon="icon-moon" icon_prefix="prefix" />);
    const icon = document.querySelector('.prefix__icon');
    expect(icon).toBeInTheDocument();
  });
  it('should be "icon--modifier" class with modifier "modifier"', () => {
    render(<Icon icon="icon-moon" icon_modifier="modifier" />);
    const icon = document.querySelector('.icon--modifier');
    expect(icon).toBeInTheDocument();
  });

  it('should be "prefix__icon--modifier" class with prefix "prefix" and modifier "modifier"', () => {
    render(
      <Icon icon="icon-moon" icon_modifier="modifier" icon_prefix="prefix" />
    );
    const icon = document.querySelector('.prefix__icon--modifier');
    expect(icon).toBeInTheDocument();
  });
});
