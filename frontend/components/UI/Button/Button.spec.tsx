import { render, screen } from '@testing-library/react';
import Button from './Button';

describe('Tests for Button component', () => {
  const buttonTypes = ['button', 'submit', 'reset'];

  for (const buttonType of buttonTypes) {
    it(`should be button with ${buttonType} type and label`, () => {
      //@ts-ignore
      render(<Button button_type={buttonType}>button</Button>);
      const button = screen.getByRole('button');
      expect(button).toBeInTheDocument();
      expect(button).toHaveAttribute('type', buttonType);
      expect(button.innerHTML).toEqual('button');
    });
  }

  it('should be proper button class with button_prefix prop', () => {
    render(
      <Button button_type="button" button_prefix="prefix">
        button
      </Button>
    );

    expect(screen.getByRole('button')).toHaveClass('prefix__button');
  });

  it('should be proper button class with button_modifier prop', () => {
    render(
      <Button button_type="button" button_modifier="modifier">
        button
      </Button>
    );

    expect(screen.getByRole('button')).toHaveClass('button--modifier');
  });

  it('should be proper button class with button_prefix and button_modifier props', () => {
    render(
      <Button
        button_type="button"
        button_prefix="prefix"
        button_modifier="modifier"
      >
        button
      </Button>
    );

    expect(screen.getByRole('button')).toHaveClass('prefix__button--modifier');
  });
});
