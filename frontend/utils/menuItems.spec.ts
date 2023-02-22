import { expect } from '@jest/globals';
// import { menuItems } from './menuItems';

import { menuItems } from './menuItemsForTests';

describe('Tests for menu items', () => {
  it('should be 4 elements', () => {
    expect(menuItems.length).toEqual(4);
  });

  it('should be "blog" in first element', () => {
    expect(menuItems[0].name).toEqual('Blog');
    expect(menuItems[0].target).toEqual('/blog');
  });
  it('should be "exercises" in second element', () => {
    expect(menuItems[1].name).toEqual('Ćwiczenia');
    expect(menuItems[1].target).toEqual('/exercises');
  });
  it('should be "glossary" in third element', () => {
    expect(menuItems[2].name).toEqual('Glosariusz');
    expect(menuItems[2].target).toEqual('/glossary');
  });
  it('should be "about me" in 4th element', () => {
    expect(menuItems[3].name).toEqual('O mnie');
    expect(menuItems[3].target).toEqual('/about');
  });
});
