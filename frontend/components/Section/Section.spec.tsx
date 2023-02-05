import { render, screen } from '@testing-library/react';
import Section from './Section';

describe('Tests for Section component', () => {
  it('should be proper section without any props', () => {
    render(
      <Section>
        <p>some text</p>
      </Section>
    );
    expect(document.querySelector('.section')).toBeInTheDocument();
    expect(screen.getByText('some text')).toBeInTheDocument();
  });
  it('should be proper section class with section_prefix prop', () => {
    render(
      <Section section_prefix="prefix">
        <p>some text</p>
      </Section>
    );
    expect(document.querySelector('.prefix__section')).toBeInTheDocument();
    expect(screen.getByText('some text')).toBeInTheDocument();
  });
  it('should be proper section class with section_modifier prop', () => {
    render(
      <Section section_modifier="modifier">
        <p>some text</p>
      </Section>
    );
    expect(document.querySelector('.section--modifier')).toBeInTheDocument();
    expect(screen.getByText('some text')).toBeInTheDocument();
  });

  it('should be proper section class with section_prefix and section_modifier props', () => {
    render(
      <Section section_modifier="modifier" section_prefix="prefix">
        <p>some text</p>
      </Section>
    );
    expect(
      document.querySelector('.prefix__section--modifier')
    ).toBeInTheDocument();
    expect(screen.getByText('some text')).toBeInTheDocument();
  });
});
