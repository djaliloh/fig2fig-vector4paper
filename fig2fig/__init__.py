"""
fig2fig-vector4paper: Convert and export research figures into publication-ready formats.

This package provides tools for creating publication-ready figures with Matplotlib
and converting raster images to vector formats.
"""

from fig2fig.exporter import FigureExporter

try:
    from fig2fig.vectorizer import vectorize_image
except ImportError:
    vectorize_image = None  # vtracer is optional

__version__ = "0.1.0"
__author__ = "Djalil"

__all__ = [
    "FigureExporter",
    "vectorize_image",
]
