"""
Example: Creating and exporting a publication-ready Matplotlib figure.

This example demonstrates how to use FigureExporter to create a simple plot
and export it in multiple formats (PDF, SVG, PNG).
"""

import numpy as np
from fig2fig import FigureExporter

# Initialize exporter with publication settings
exporter = FigureExporter(font_family="sans-serif", font_size=10)

# Create a figure with standard single-column width
fig, ax = exporter.create_figure(width=3.5, height=2.8)

# Generate and plot data
x = np.linspace(0, 10, 100)
y = np.sin(x)

ax.plot(x, y, label=r"Signal $\sin(x)$", color="#1f77b4", linewidth=1.5)
ax.axhline(0, color="gray", linestyle="--", linewidth=0.8)

# Add annotation with arrow
ax.annotate(
    "Peak",
    xy=(np.pi / 2, 1),
    xytext=(np.pi / 2 + 1, 0.8),
    arrowprops=dict(facecolor="black", shrink=0.05, width=1, headwidth=4),
)

# Configure axes
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude (a.u.)")
ax.set_title("Response Diagram")
ax.legend(frameon=False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Export in multiple formats
exporter.save(fig, "output_figure", formats=["pdf", "svg", "png"])

exporter.close_all()
