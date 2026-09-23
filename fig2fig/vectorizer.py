"""
Raster-to-vector image conversion using vtracer.

This module provides functionality to convert PNG/JPEG diagrams to scalable SVG format.
Requires the optional 'vtracer' dependency.
"""

from pathlib import Path
from typing import Literal

try:
    import vtracer
except ImportError:
    vtracer = None


def vectorize_image(
    input_path: str | Path,
    output_path: str | Path,
    colormode: Literal["color", "bw"] = "color",
    filter_speckle: int = 4,
    color_precision: int = 6,
    layer_difference: int = 16,
) -> None:
    """
    Convert a raster image (PNG, JPEG) to a scalable SVG vector format.

    This function uses vtracer to trace raster images and convert them to
    high-quality vector graphics. Useful for converting diagrams, screenshots,
    or scanned figures.

    Args:
        input_path: Path to input image (PNG, JPEG, etc.)
        output_path: Path for output SVG file
        colormode: Color mode for tracing ('color' or 'bw' for black & white)
        filter_speckle: Speckle filter threshold (0-10). Higher = more aggressive
        color_precision: Color precision for color mode (1-10)
        layer_difference: Layer difference for color clustering (0-255)

    Raises:
        ImportError: If vtracer is not installed
        FileNotFoundError: If input file doesn't exist
        ValueError: If colormode is invalid

    Examples:
        >>> vectorize_image("diagram.png", "diagram.svg", colormode="color")
        >>> vectorize_image("scan.jpg", "scan_vector.svg", colormode="bw", filter_speckle=4)

    Note:
        Requires vtracer to be installed. Install with:
        $ uv pip install fig2fig-vector4paper[vectorize]
    """
    if vtracer is None:
        raise ImportError(
            "vtracer is not installed. Install it with:\n"
            "  uv pip install fig2fig-vector4paper[vectorize]\n"
            "or\n"
            "  pip install vtracer"
        )

    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input image not found: {input_path}")

    if colormode not in ("color", "bw"):
        raise ValueError("colormode must be 'color' or 'bw'")

    # Create output directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Vectorize the image
    vtracer.convert_image_to_svg_py(
        str(input_path),
        str(output_path),
        colormode=colormode,
        filter_speckle=filter_speckle,
        color_precision=color_precision,
        layer_difference=layer_difference,
    )

    print(f"✓ Vectorized: {input_path} → {output_path}")
