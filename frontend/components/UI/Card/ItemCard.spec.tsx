import { render, screen } from '@testing-library/react';
import ItemCard from './ItemCard';

describe('Tests for ItemCard component', () => {
  it('should be item-card class without any props', () => {
    render(
      <ItemCard>
        <p>some content</p>
      </ItemCard>
    );
    expect(document.querySelector('.item-card')).toBeInTheDocument();
    expect(screen.getByText('some content')).toBeInTheDocument();
  });

  it('should be proper class  with itemCard_prefix props', () => {
    render(
      <ItemCard itemCard_prefix="prefix">
        <p>some content</p>
      </ItemCard>
    );
    expect(document.querySelector('.prefix__item-card')).toBeInTheDocument();
    expect(screen.getByText('some content')).toBeInTheDocument();
  });
  it('should be proper class  with itemCard_modifier props', () => {
    render(
      <ItemCard itemCard_modifier="modifier">
        <p>some content</p>
      </ItemCard>
    );
    expect(document.querySelector('.item-card--modifier')).toBeInTheDocument();
    expect(screen.getByText('some content')).toBeInTheDocument();
  });

  it('should be proper class  with itemCard_modifier and itemCard_prefix  props', () => {
    render(
      <ItemCard itemCard_modifier="modifier" itemCard_prefix="prefix">
        <p>some content</p>
      </ItemCard>
    );
    expect(
      document.querySelector('.prefix__item-card--modifier')
    ).toBeInTheDocument();
    expect(screen.getByText('some content')).toBeInTheDocument();
  });
});
