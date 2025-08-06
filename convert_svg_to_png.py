
from pathlib import Path
import cairosvg

def convert_svg_to_png(svg_path: str, png_path: str) -> bool:
    """Convert SVG file to PNG format."""
    try:
        svg_file = Path(svg_path)
        if not svg_file.exists():
            raise FileNotFoundError(f"SVG file not found: {svg_path}")
        cairosvg.svg2png(url=str(svg_file), write_to=png_path)
        print(f"Converted {svg_path} to {png_path}")
        return True
    except Exception as e:
        print(f"Error converting SVG to PNG: {e}")
        return False
