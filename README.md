# fig2fig-vector4paper

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**fig2fig-vector4paper** is a Python toolkit designed to convert and export research figures into publication-ready, high-resolution vector formats (**PDF, SVG**) and high-DPI raster images (**PNG, JPEG**).

It ensures crisp graphics, fully scalable embedded text (Type 42 fonts), and standard layout configurations compliant with most scientific journals and conferences.

---

## Key Features 

- **Publication-Ready Defaults:** Configures Matplotlib to export text as true vector paths (no pixelated labels or font substitution errors in LaTeX).
- **Multi-Format Export:** One-line export to `PDF`, `SVG`, `PNG` (300+ DPI), and `JPEG`.
- **Automatic Raster-to-Vector Pipeline:** Built-in support for vectorizing raster diagrams using `vtracer`.
- **Publisher Layout Presets:** Pre-defined figure dimensions for single-column and double-column formats.

---

## Installation 

### Quick Start with `uv` (Recommended)

[`uv`](https://github.com/astral-sh/uv) is a fast Python package manager. Install the project:

```bash
git clone https://github.com/djaliloh/fig2fig-vector4paper.git
cd fig2fig-vector4paper
uv pip install -e .
```

### With Optional Dependencies

For image vectorization (PNG/JPEG → SVG):

```bash
uv pip install -e ".[vectorize]"
```

For development (tests, linting, type checking):

```bash
uv pip install -e ".[dev]"
```

### Traditional pip

If you don't have `uv` installed:

```bash
pip install -e .
```

---

## Dependencies

**Core:**
- `matplotlib` (≥3.8.0) — Figure creation and styling
- `numpy` (≥1.24.0) — Numerical operations

**Optional:**
- `vtracer` (≥0.1.8) — Raster-to-vector image conversion
- `pytest`, `black`, `ruff`, `mypy` — Development tools

## Quick Start 

### 1. Creating Publication-Ready Figures

Use `FigureExporter` to create and export figures with publication-quality settings:

```python
import numpy as np
from fig2fig import FigureExporter

# Initialize exporter with publication settings
exporter = FigureExporter(font_family="sans-serif", font_size=10)

# Create a figure with standard single-column width (3.5 inches)
fig, ax = exporter.create_figure(width=3.5, height=2.8)

# Plot your data
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), label=r"Signal $\sin(x)$", color="#1f77b4")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude")
ax.set_title("Response Curve")
ax.legend()

# Export in multiple formats with one call
exporter.save(fig, "output_figure", formats=["pdf", "svg", "png"])
```

### 2. Converting Images to Vector Format

Vectorize existing PNG/JPEG diagrams to scalable SVG:

```python
from fig2fig import vectorize_image

# Requires: uv pip install fig2fig-vector4paper[vectorize]
vectorize_image(
    input_path="diagram.png",
    output_path="diagram.svg",
    colormode="color",     # 'color' or 'bw'
    filter_speckle=4       # Noise reduction
)
```

### 3. Using Size Presets

Built-in presets for common journal formats:

```python
# Single column (Nature, IEEE: 3.5")
fig, ax = exporter.create_figure(size_preset="single")

# Double column (full page: 7.0")
fig, ax = exporter.create_figure(size_preset="double")

# Square (4.0" × 4.0")
fig, ax = exporter.create_figure(size_preset="square")
```

## Testing

Run the test suite:

```bash
# Install dev dependencies
uv pip install -e ".[dev]"

# Run all tests
pytest tests/

# Run with coverage report
pytest tests/ --cov=fig2fig --cov-report=html
```

**Test Coverage:**
- ✅ FigureExporter initialization and configuration
- ✅ Figure creation with presets and custom sizes
- ✅ Multi-format export (PDF, SVG, PNG, JPEG)
- ✅ Image vectorization with vtracer
- ✅ Error handling and edge cases

---

## Code Quality

Format and lint your code:

```bash
# Format with black
black fig2fig/ examples/ tests/

# Lint with ruff
ruff check fig2fig/ examples/ tests/

# Type checking with mypy
mypy fig2fig/
```

---

## Contributing 

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/djaliloh/fig2fig-vector4paper/issues).

### Development Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make changes and ensure tests pass: `pytest tests/`
4. Format code: `black fig2fig/ tests/`
5. Submit a pull request