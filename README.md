# Single Path Art Generator

## Overview
This project provides a Python function `create_svg_content_with_curve` that converts a grayscale image into a single-path SVG artwork. The generated SVG uses smooth quadratic Bézier curves to create a visually appealing representation of the image, where pixel intensities influence sinusoidal wave patterns.

please see: https://github.com/innolab-mn/single_line_svg/blob/main/Single_rect_line.ipynb

## Features
- **Input**: Accepts a 2D NumPy array (`image_gray`) representing a grayscale image.
- **Output**: Generates an SVG file with a single continuous path that approximates sinusoidal segments.
- **Customization**: Allows adjustment of parameters like `sin_width`, `sin_height`, `sin_height_correction`, and `stroke_width` to control the wave's appearance.
- **Validation**: Ensures input image is a valid 2D NumPy array with positive dimensions and checks for positive `sin_width` and `sin_height`.

## How It Works
1. **Input Validation**: The function verifies that the input `image_gray` is a valid 2D NumPy array and that its dimensions and parameters are positive.
2. **SVG Initialization**: Creates an SVG canvas matching the input image's dimensions with a white background.
3. **Path Generation**:
   - Iterates over the image rows in steps of `2 * sin_height`.
   - For each row, constructs a single continuous path starting at the left edge.
   - Uses pixel intensities to modulate the amplitude of sinusoidal waves, achieved through cubic Bézier curves.
   - Each segment is defined by control points (`x1, y1`, `x3, y3`, `x4, y4`) to approximate a smooth sine wave, where the intensity (normalized between 0 and 1) adjusts the wave height via `sin_height_correction`.
4. **Output**: Produces SVG content as a string, which can be saved as an `.svg` file for viewing or further processing.

## Parameters
- `image_gray` (Optional[np.ndarray]): A 2D NumPy array representing the grayscale image. Pixel values (0–255) determine wave amplitude.
- `sin_width` (float): The horizontal distance between wave segments (default: 3).
- `sin_height` (float): The vertical spacing between rows of waves (default: 4).
- `sin_height_correction` (float): Scales the wave amplitude based on pixel intensity (default: 8).
- `stroke_width` (float): Thickness of the SVG path (default: 1).

## Usage Example
```python
import numpy as np
import cv2
from create_svg_content_with_curve import create_svg_content_with_curve

image = cv2.imread(image_path)

# Convert the image to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Generate SVG content
svg_content = create_svg_content_with_curve(
    image_gray=image,
    sin_width=3,
    sin_height=4,
    sin_height_correction=8,
    stroke_width=1
)

# Save to file
with open("output.svg", "w") as f:
    f.write(svg_content)