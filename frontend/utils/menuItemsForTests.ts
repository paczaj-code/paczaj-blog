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
