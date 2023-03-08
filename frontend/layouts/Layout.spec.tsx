import { render, screen } from '@testing-library/react';
import Layout from './Layout';

describe('Tests for Layout component', () => {
  it('should be proper section without any props', () => {
    render(
      <Layout layout_prefix="prefix" layout_modifier="modifier">
        <p>some text</p>
      </Layout>
    );
    expect(document.querySelector('main')).toBeInTheDocument();
    expect(document.querySelector('main')).toHaveClass(
      'prefix__layout--modifier'
    );
    expect(screen.getByText('some text')).toBeInTheDocument();
  });
});
