"""Unit tests for fig2fig.exporter module."""

import tempfile
from pathlib import Path

import matplotlib.pyplot as plt
import pytest

from fig2fig import FigureExporter


class TestFigureExporter:
    """Test suite for FigureExporter class."""

    def test_init_creates_output_dir(self):
        """Test that __init__ creates output directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "figures"
            exporter = FigureExporter(output_dir=output_dir)
            assert output_dir.exists()

    def test_init_with_custom_font(self):
        """Test initialization with custom font settings."""
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = FigureExporter(
                font_family="monospace",
                font_size=12,
                output_dir=tmpdir
            )
            assert exporter.font_family == "monospace"
            assert exporter.font_size == 12

    def test_create_figure_with_custom_size(self):
        """Test creating figure with custom dimensions."""
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = FigureExporter(output_dir=tmpdir)
            fig, ax = exporter.create_figure(width=5.0, height=3.0)

            assert fig.get_figwidth() == 5.0
            assert fig.get_figheight() == 3.0
            plt.close(fig)

    def test_create_figure_with_preset(self):
        """Test creating figure with size preset."""
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = FigureExporter(output_dir=tmpdir)
            fig, ax = exporter.create_figure(size_preset="single")

            assert fig.get_figwidth() == 3.5
            assert fig.get_figheight() == 2.8
            plt.close(fig)

    def test_create_figure_invalid_preset(self):
        """Test that invalid preset raises ValueError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = FigureExporter(output_dir=tmpdir)
            with pytest.raises(ValueError, match="Unknown preset"):
                exporter.create_figure(size_preset="invalid")

    def test_save_single_format(self):
        """Test saving figure in single format."""
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = FigureExporter(output_dir=tmpdir)
            fig, ax = exporter.create_figure()
            ax.plot([1, 2, 3], [1, 2, 3])

            exporter.save(fig, "test_figure", formats=["pdf"])

            output_file = Path(tmpdir) / "test_figure.pdf"
            assert output_file.exists()
            assert output_file.stat().st_size > 0
            plt.close(fig)

    def test_save_multiple_formats(self):
        """Test saving figure in multiple formats."""
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = FigureExporter(output_dir=tmpdir)
            fig, ax = exporter.create_figure()
            ax.plot([1, 2, 3], [1, 2, 3])

            formats = ["pdf", "svg", "png"]
            exporter.save(fig, "test_figure", formats=formats)

            for fmt in formats:
                output_file = Path(tmpdir) / f"test_figure.{fmt}"
                assert output_file.exists()
                assert output_file.stat().st_size > 0
            plt.close(fig)

    def test_save_unsupported_format(self):
        """Test that unsupported format raises ValueError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = FigureExporter(output_dir=tmpdir)
            fig, ax = exporter.create_figure()

            with pytest.raises(ValueError, match="Unsupported format"):
                exporter.save(fig, "test_figure", formats=["xyz"])
            plt.close(fig)

    def test_save_with_custom_dpi(self):
        """Test saving with custom DPI."""
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = FigureExporter(output_dir=tmpdir)
            fig, ax = exporter.create_figure()
            ax.plot([1, 2, 3], [1, 2, 3])

            exporter.save(fig, "test_figure", formats=["png"], dpi=150)

            output_file = Path(tmpdir) / "test_figure.png"
            assert output_file.exists()
            plt.close(fig)

    def test_save_jpeg_alias(self):
        """Test that 'jpg' format is aliased to 'jpeg'."""
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = FigureExporter(output_dir=tmpdir)
            fig, ax = exporter.create_figure()
            ax.plot([1, 2, 3], [1, 2, 3])

            exporter.save(fig, "test_figure", formats=["jpg"])

            output_file = Path(tmpdir) / "test_figure.jpeg"
            assert output_file.exists()
            plt.close(fig)

    def test_close_all(self):
        """Test closing all figures."""
        exporter = FigureExporter()
        fig, ax = exporter.create_figure()
        exporter.create_figure()

        exporter.close_all()

        assert len(plt.get_fignums()) == 0
