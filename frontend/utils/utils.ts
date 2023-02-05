export const classNameModifiers = (
  prefix: string | undefined,
  modifier: string | undefined,
  className: string
) => {
  const class_prefix = prefix ? `${prefix}__` : '';
  const class_modifier = modifier ? `--${modifier}` : '';

  return `${class_prefix}${className}${class_modifier}`;
};
