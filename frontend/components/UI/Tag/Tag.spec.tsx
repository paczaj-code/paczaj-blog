import { render, screen, fireEvent } from '@testing-library/react';
import Tag from './Tag';

const onClick = jest.fn();

describe('Tests for Tag component', () => {
  it('should be proper section without any props', () => {
    render(
      <Tag
        name="tag"
        slug="tab-slug"
        tag_prefix="prefix"
        tag_modifier="modifier"
        isActive={true}
      />
    );

    expect(document.querySelector('span')).toBeInTheDocument();
    expect(document.querySelector('span')).toHaveClass('prefix__tag--active');
  });

  it('should be proper section without any props', () => {
    render(<Tag name="tag" slug="tab-slug" tag_prefix="prefix" />);

    expect(document.querySelector('span')).toBeInTheDocument();
    expect(document.querySelector('span')).toHaveClass('prefix__tag');
  });

  it('should be proper section without any props', () => {
    render(
      <Tag
        name="tag"
        slug="tab-slug"
        tag_prefix="prefix"
        tag_modifier="modifier"
        onClick={onClick}
      />
    );

    const tag = screen.getByTestId('tag');
    fireEvent.click(tag);
    expect(onClick).toBeCalledTimes(1);
  });
});
