"""
Main module for exporting Matplotlib figures to publication-ready formats.

Provides the FigureExporter class for creating and exporting figures in
PDF, SVG, PNG, and JPEG formats with publication-quality settings.
"""

from pathlib import Path
from typing import Literal, Sequence

import matplotlib.pyplot as plt
import numpy as np

from fig2fig.config import DEFAULT_FIGURE_SIZES, DPI_SETTINGS, PUBLICATION_RCPARAMS


class FigureExporter:
    """
    A wrapper around Matplotlib for creating publication-ready figures.

    This class provides convenience methods for styling figures according to
    publication standards and exporting them in multiple formats.

    Attributes:
        font_family (str): Font family for figures (default: "sans-serif")
        font_size (int): Base font size in points (default: 10)
        output_dir (Path): Directory for saving figures
    """

    def __init__(
        self,
        font_family: str = "sans-serif",
        font_size: int = 10,
        output_dir: str | Path = ".",
    ):
        """
        Initialize the FigureExporter with publication settings.

        Args:
            font_family: Font family to use (default: "sans-serif")
            font_size: Base font size in points (default: 10)
            output_dir: Directory where figures will be saved (default: current dir)
        """
        self.font_family = font_family
        self.font_size = font_size
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self._apply_publication_style()

    def _apply_publication_style(self) -> None:
        """Apply publication-quality rcParams to Matplotlib."""
        rcparams = PUBLICATION_RCPARAMS.copy()
        rcparams["font.family"] = self.font_family
        rcparams["font.size"] = self.font_size
        plt.rcParams.update(rcparams)

    def create_figure(
        self,
        width: float | None = None,
        height: float | None = None,
        size_preset: str = "single",
        **kwargs,
    ) -> tuple:
        """
        Create a figure with standard publication dimensions.

        Args:
            width: Figure width in inches. If None, uses size_preset.
            height: Figure height in inches. If None, uses size_preset.
            size_preset: Preset size name ('single', 'single_tall', 'double', 'square').
                        Ignored if width/height are provided.
            **kwargs: Additional arguments passed to plt.subplots()

        Returns:
            Tuple of (fig, ax) from plt.subplots()

        Examples:
            >>> exporter = FigureExporter()
            >>> fig, ax = exporter.create_figure(width=3.5, height=2.8)
            >>> fig, ax = exporter.create_figure(size_preset="single")
        """
        if width is None or height is None:
            if size_preset not in DEFAULT_FIGURE_SIZES:
                raise ValueError(
                    f"Unknown preset '{size_preset}'. "
                    f"Choose from: {list(DEFAULT_FIGURE_SIZES.keys())}"
                )
            width, height = DEFAULT_FIGURE_SIZES[size_preset]

        fig, ax = plt.subplots(figsize=(width, height), dpi=100, **kwargs)
        return fig, ax

    def save(
        self,
        fig,
        output_name: str,
        formats: Sequence[str] | None = None,
        dpi: int | None = None,
        bbox_inches: str = "tight",
        **kwargs,
    ) -> None:
        """
        Save a figure in multiple formats.

        Args:
            fig: Matplotlib figure object to save
            output_name: Base name for output files (without extension)
            formats: List of formats to save in (default: ["pdf", "svg", "png"]).
                    Supported: "pdf", "svg", "png", "jpeg", "jpg"
            dpi: DPI for raster formats. If None, uses DPI_SETTINGS per format.
            bbox_inches: Bounding box in inches (default: "tight")
            **kwargs: Additional arguments passed to fig.savefig()

        Examples:
            >>> exporter.save(fig, "my_figure", formats=["pdf", "svg", "png"])
            >>> exporter.save(fig, "plot", formats=["png"], dpi=600)
        """
        if formats is None:
            formats = ["pdf", "svg", "png"]

        for fmt in formats:
            fmt = fmt.lower().lstrip(".")
            if fmt == "jpg":
                fmt = "jpeg"

            if fmt not in DPI_SETTINGS:
                raise ValueError(f"Unsupported format: {fmt}")

            output_dpi = dpi if dpi is not None else DPI_SETTINGS[fmt]
            output_path = self.output_dir / f"{output_name}.{fmt}"

            fig.savefig(
                str(output_path),
                format=fmt,
                dpi=output_dpi,
                bbox_inches=bbox_inches,
                **kwargs,
            )
            print(f"✓ Saved: {output_path}")

    def close_all(self) -> None:
        """Close all figure windows."""
        plt.close("all")
