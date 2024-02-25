# dad-concat-util

Utility to quickly concatenate images into a grid of a specified size.

Basic usage:

``` sh
dad-concat-util --input-dir <path-to-images> --n-rows <N> --output-dir <...>
```

## Options

This script works by creating several rows of images (when `n-rows > 1`), and
then joining each row vertically. Below are options that can modify the behavior
of the script.

- `--input-dir <directory>`: Required. Directory containing images to put into a
  grid
- `--n-rows <N>`: Default: 1. Specifies how many rows the grid will contain. If
  you have a 25 images but choose 6 rows, the last row will only have 1 image.
- `--output-dir <N>`: Default: `$HOME`. Specify where to place the resulting
  image.
-`--resize-heights`: Default: True. When True, resizes images in a row to all
  have the same height, keeping the same aspect ratio
- `--no-resize-heights`: Turn off resizing when forming a row of images
- `--resize-widths`: Default: True.
- `--no-resize-widths`: Turn off resizing when joining rows of images
- `--center-horizontally`: When joining rows of images, center them along the
  Y-axis. Only applicable when `--no-resize-widths` is specified
- `--no-center-horizontally`: Do not center rows of images
- `--center-vertically`:  When forming a row of images, center them vertically
  along the X-axis. Only applicable when `--no-resize-heights` is specified. Not
  recommended, since it will leave empty space above and below a row if the
  images aren't all the same size.
- `--no-center-vertically`: Do not center images in a row.

Recommended options:

1. Basic Operation (Resize everything)
``` sh
dad-concat-util --input-dir <path-to-images> --n-rows <N> --output-dir <...>
```

2. Resize within a row, but not across rows, and center rows vertically:
``` sh
dad-concat-util --input-dir <path-to-images> --n-rows <N> --output-dir <...> \
  --resize-heights
  --no-resize-widths
```

3. Don't Resize, don't center:
``` sh
dad-concat-util --input-dir <path-to-images> --n-rows <N> --output-dir <...> \
  --no-resize-heights
  --no-resize-widths
  --no-center-horizontally
  --no-center-vertically
```

It is recommended to create bash aliases for preferred operations.

Contact @prinzi_8932 on Discord for any questions

