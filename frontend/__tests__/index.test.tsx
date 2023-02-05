import { render, screen } from '@testing-library/react';
import Home from '@/pages/index';

describe('Home', () => {
  it('should be equal', () => {
    expect(2).toEqual(2);
  });
  it('renders a heading', () => {
    render(<Home />);

    const heading = screen.getAllByRole('heading', { level: 1 });

    expect(heading[0]).toBeInTheDocument();
  });
});
