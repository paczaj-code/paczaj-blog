interface MenuItemTypes {
  name: string;
  target: string;
  icon?: string;
}

export interface MenuTypes extends MenuItemTypes {
  subMenu?: { name: string; icon?: string; subMenuItems: MenuItemTypes[] };
}

export const menuItems = [
  {
    name: 'Blog',
    target: '/blog',
    icon: undefined,
    subMenu: [
      {
        name: 'Bazy danych',
        icon: 'icon-data',
        subMenuItems: [
          {
            name: 'SQL',
            target: '/sql',
            icon: 'icon-microsoftsqlserver',
          },
          { name: 'MongoDB', target: '/mongodb', icon: 'icon-mongodb' },
        ],
      },
      {
        name: 'DataScience',
        icon: 'icon-linegraph',
        subMenuItems: [
          { name: 'Pandas', target: '/pandas', icon: 'icon-pandas' },
          { name: 'NumPy', target: '/numpy', icon: 'icon-numpy' },
        ],
      },
    ],
  },
  {
    name: 'Ćwiczenia',
    target: '/exercises',
    icon: undefined,
    subMenu: [
      {
        name: 'Bazy danych',
        icon: 'icon-data',
        subMenuItems: [
          { name: 'SQL', target: '/sql', icon: 'icon-microsoftsqlserver' },
          { name: 'MongoDB', target: '/mongodb', icon: 'icon-mongodb' },
        ],
      },
      {
        name: 'DataScience',
        icon: 'icon-linegraph',
        subMenuItems: [
          { name: 'Pandas', target: '/pandas', icon: 'icon-pandas' },
          { name: 'NumPy', target: '/numpy', icon: 'icon-numpy' },
        ],
      },
    ],
  },
  { name: 'Glosariusz', target: '/glossary', icon: undefined },
  { name: 'O mnie', target: '/about', icon: undefined },
];

// "subcategories": [
//   {
//     "id": 3,
//     "name": "MongoDB",
//     "icon": "icon-mongodb",
//     "slug": "mongodb",
//     "posts": 0,
//     "subcount": 0
//   },
//   {
//     "id": 2,
//     "name": "SQL",
//     "icon": "icon-microsoftsqlserver-color",
//     "slug": "sql",
//     "posts": 0,
//     "description": "<h2>\r\n  REalcujne naa\r\n</h2>",
//     "subcount": 0
//   }
// ],
