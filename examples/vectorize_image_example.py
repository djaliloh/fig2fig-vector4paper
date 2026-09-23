"""
Example: Converting raster images to vector SVG format.

This example shows how to use vectorize_image to convert PNG/JPEG diagrams
to scalable SVG format. Images are expected to be in the images_test/ directory.

Requires vtracer to be installed:
    uv pip install fig2fig-vector4paper[vectorize]
"""

from pathlib import Path

from fig2fig import vectorize_image

# Paths to test images
images_dir = Path(__file__).parent.parent / "images_test"
output_dir = Path(__file__).parent.parent / "output"

# Create output directory
output_dir.mkdir(exist_ok=True)

# Process test images
test_images = [
    "all_in_one_test.png",
    "archifull_test.png",
]

for image_name in test_images:
    input_path = images_dir / image_name
    if not input_path.exists():
        print(f"⚠ Image not found: {input_path}")
        continue

    # Convert to SVG (color mode)
    output_svg = output_dir / image_name.replace(".png", ".svg")
    try:
        vectorize_image(
            input_path,
            output_svg,
            colormode="color",
            filter_speckle=4,
        )
    except ImportError as e:
        print(f"✗ Error: {e}")
        print("  Install vtracer with: uv pip install fig2fig-vector4paper[vectorize]")
        break
