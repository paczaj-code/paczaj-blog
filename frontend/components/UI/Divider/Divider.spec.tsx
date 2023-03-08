import { render, screen } from '@testing-library/react';
import Divider from './Divider';
describe('Tests for Divider component', () => {
  it('should be proper section without any props', () => {
    render(<Divider divider_prefix="prefix" divider_modifier="modifier" />);

    expect(document.querySelector('hr')).toBeInTheDocument();
    expect(document.querySelector('hr')).toHaveClass(
      'prefix__divider--modifier'
    );
  });
});
