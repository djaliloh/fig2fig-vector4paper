"""
Publication-ready figure configuration presets and constants.

This module provides standard figure dimensions for different publication formats
and recommended settings for matplotlib rendering.
"""

# Standard column widths (in inches) for common scientific journals
COLUMN_WIDTHS = {
    "single": 3.5,  # Single column (e.g., Nature, IEEE)
    "double": 7.0,  # Double column (full page width)
    "half": 1.75,  # Half column
}

# Default figure dimensions (width, height) in inches
DEFAULT_FIGURE_SIZES = {
    "single": (3.5, 2.8),
    "single_tall": (3.5, 4.2),
    "double": (7.0, 3.5),
    "square": (4.0, 4.0),
}

# DPI settings for different export formats
DPI_SETTINGS = {
    "pdf": 300,
    "svg": 300,
    "png": 300,
    "jpeg": 300,
    "screen": 100,
}

# Default matplotlib rcParams for publication-quality figures
PUBLICATION_RCPARAMS = {
    # Vector text rendering in PDF/PS/SVG
    "pdf.fonttype": 42,  # Embed fonts as Type 42 (TrueType)
    "ps.fonttype": 42,
    "svg.fonttype": "path",  # Render text as paths in SVG
    # Font settings
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica"],
    "font.size": 10,
    "axes.labelsize": 11,
    "axes.titlesize": 12,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    # Figure layout
    "figure.autolayout": True,
    "figure.dpi": 100,  # Screen display DPI
    # Rendering
    "lines.linewidth": 1.0,
    "patch.linewidth": 0.5,
    "axes.linewidth": 0.8,
    "axes.labelpad": 3.0,
    "axes.spines.top": False,
    "axes.spines.right": False,
    # Legend
    "legend.frameon": False,
    "legend.numpoints": 1,
    # Grid
    "axes.grid": False,
}
