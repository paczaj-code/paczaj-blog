import { render, screen } from '@testing-library/react';
import Heading from './Heading';

describe('Tests for Heading component', () => {
  const headingTags = [
    { tag: 'h1', level: 1 },
    { tag: 'h2', level: 2 },
    { tag: 'h3', level: 3 },
    { tag: 'h4', level: 4 },
    { tag: 'h5', level: 5 },
    { tag: 'h6', level: 6 },
  ];
  for (const headingTag of headingTags) {
    it(`should be proper heading tag ${headingTag.tag}`, () => {
      render(<Heading headingLevel={headingTag.tag} heading_label="Heading" />);
      expect(
        screen.getByRole('heading', { level: headingTag.level })
      ).toBeInTheDocument();
    });
  }

  it('should be proper label', () => {
    render(<Heading headingLevel="h2" heading_label="Heading" />);
    expect(screen.getByText('Heading')).toBeInTheDocument();
  });

  it('should be icon with icon prop', () => {
    render(
      <Heading
        headingLevel="h2"
        heading_label="Heading"
        heading_icon="icon-moon"
      />
    );
    expect(document.querySelector('.icon-moon')).toBeInTheDocument();
  });
});
