import numpy as np
from typing import Optional
from typing import Optional
import numpy as np

def create_svg_content_with_curve(image_gray: Optional[np.ndarray] = None, 
                                  sin_width=3, 
                                  sin_height=4, 
                                  sin_height_correction=8,
                                  stroke_width=1):
    """Create a single continuous serpentine SVG path using smooth cubic Bézier curves."""

    # --- Validation ---
    if not isinstance(image_gray, np.ndarray) or image_gray.ndim != 2:
        raise ValueError("image_gray must be a 2D NumPy array")

    height, width = image_gray.shape
    if width <= 0 or height <= 0:
        raise ValueError("Image dimensions must be positive")
    if sin_width <= 0 or sin_height <= 0:
        raise ValueError("sin_width and sin_height must be positive")

    # --- SVG header ---
    svg_parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">',
        '<rect width="100%" height="100%" fill="white"/>'
    ]

    # --- Path building ---
    path_segments = []
    first_move = True

    for row_index, i in enumerate(range(0, height, 2 * sin_height)):
        direction = 1 if row_index % 2 == 0 else -1
        col_range = range(0, width, sin_width) if direction == 1 else range(width - 1, -1, -sin_width)

        # Move or connect to start of row
        start_x = col_range.start if direction == 1 else col_range.stop + 1
        if first_move:
            path_segments.append(f"M{col_range[0]},{i}")
            first_move = False
        else:
            path_segments.append(f"L{col_range[0]},{i}")

        # Curve drawing
        for j in col_range:
            node_density = 1 - image_gray[i, j] / 255.0
            dx = direction * sin_width

            x1 = j + dx / 4
            y1 = i + node_density * sin_height_correction
            x3 = j + dx * 3 / 4
            y3 = i - node_density * sin_height_correction
            x4 = j + dx
            y4 = i

            path_segments.append(f"C{x1},{y1} {x3},{y3} {x4},{y4}")

    # --- Add path to SVG ---
    svg_parts.append(f'<path d="{" ".join(path_segments)}" stroke="black" stroke-width="{stroke_width}" fill="none"/>')
    svg_parts.append("</svg>")

    return "\n".join(svg_parts)
