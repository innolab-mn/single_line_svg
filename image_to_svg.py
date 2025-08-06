
from typing import Optional
import numpy as np

def create_svg_content_with_curve(image_gray: Optional[np.ndarray] = None, 
                                  sin_width = 3, 
                                  sin_height = 4, 
                                  sin_height_correction = 8,
                                  stroke_width = 1
                                  ):
    """Create an SVG with smooth quadratic Bézier curves based on image_gray pixel intensities."""

    # Validate image_gray
    if not isinstance(image_gray, np.ndarray) or image_gray.ndim != 2:
        raise ValueError("image_gray must be a 2D NumPy array")
    
    width = image_gray.shape[1]
    height = image_gray.shape[0]
    if width <= 0 or height <= 0:
        raise ValueError("Image dimensions must be positive")
    
    
    
    if sin_width <= 0 or sin_height <= 0:
        raise ValueError("sin_width and sin_height must be positive")

    # Initialize SVG content
    svg_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
<rect width="100%" height="100%" fill="white"/>
"""
    for i in range(0, height, 2 * sin_height):
        path_data = f"M0,{i}"  # Start at left edge of row
        for j in range(0, width, sin_width):
            # Get node density from image_gray
            node_density = 1 - image_gray[i, j] / 255.0
            
            # Define points for a cubic Bézier curve to approximate a sine wave
            x1 = j + sin_width / 4
            y1 = i + node_density * sin_height_correction
            # x2 = j + sin_width / 2
            # y2 = i
            x3 = j + 3 * sin_width / 4
            y3 = i - node_density * sin_height_correction
            x4 = j + sin_width
            y4 = i
            
            # Use cubic Bézier to create smooth sinusoidal segment
            path_data += f" C{x1},{y1} {x3},{y3} {x4},{y4}"
        
        # Add the path to SVG content
        svg_content += f'<path d="{path_data}" stroke="black" stroke-width="{stroke_width}" fill="none"/>\n'
    svg_content += '</svg>'
    return svg_content
    
