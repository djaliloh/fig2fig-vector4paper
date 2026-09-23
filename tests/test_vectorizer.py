"""Unit tests for fig2fig.vectorizer module."""

import tempfile
from pathlib import Path

import pytest

from fig2fig import vectorize_image


class TestVectorizeImage:
    """Test suite for vectorize_image function."""

    def test_vectorize_image_import(self):
        """Test that vectorize_image is available."""
        assert vectorize_image is not None

    def test_vectorize_image_nonexistent_input(self):
        """Test that nonexistent input file raises FileNotFoundError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            input_path = Path(tmpdir) / "nonexistent.png"
            output_path = Path(tmpdir) / "output.svg"

            with pytest.raises(FileNotFoundError):
                vectorize_image(input_path, output_path)

    def test_vectorize_image_invalid_colormode(self):
        """Test that invalid colormode raises ValueError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a minimal test PNG
            try:
                from PIL import Image
                img = Image.new("RGB", (100, 100), color="red")
                input_path = Path(tmpdir) / "test.png"
                img.save(input_path)

                output_path = Path(tmpdir) / "output.svg"

                with pytest.raises(ValueError, match="colormode must be"):
                    vectorize_image(input_path, output_path, colormode="invalid")
            except ImportError:
                pytest.skip("PIL not installed")

    def test_vectorize_image_creates_output_dir(self):
        """Test that output directory is created if it doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            try:
                from PIL import Image
                img = Image.new("RGB", (100, 100), color="blue")
                input_path = Path(tmpdir) / "test.png"
                img.save(input_path)

                output_dir = Path(tmpdir) / "subdir" / "output"
                output_path = output_dir / "output.svg"

                vectorize_image(input_path, output_path, colormode="bw")

                assert output_dir.exists()
                assert output_path.exists()
            except ImportError:
                pytest.skip("PIL not installed")
