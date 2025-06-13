"""
Color Palette

A color palette is defined by its swatches. A swatch is an appropriate
sampling of colors in the palette. To maximise the difference between
colors, it is often better to choose the shortest swatch possible. This
means that the palette space is sparsely sampled.

All swatches of a palette have different lengths, are listed shortest to
longest and each swatch is longer than the previous by one color.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import cached_property
from typing import TYPE_CHECKING

from .._colormaps import PaletteInterpolatedMap
from .._colormaps._colormap import ColorMapKind

if TYPE_CHECKING:
    from mizani.typing import (
        RGB256Color,
        RGB256Swatch,
        RGB256Swatches,
        RGBHexColor,
        RGBHexSwatch,
    )

PaletteKind = ColorMapKind


@dataclass
class palette:
    #: Name of palette
    name: str

    #: Discrete samplings of the palette space
    swatches: RGB256Swatches

    #: Kind of palette
    kind: PaletteKind

    #: Number of colors in the shortest swatch
    min_colors: int = field(init=False)

    #: Number of colors in the longest swatch
    max_colors: int = field(init=False)

    def __post_init__(self):
        self.min_colors = len(self.swatches[0])
        self.max_colors = len(self.swatches[-1])

    def get_swatch(self, num_colors: int) -> RGB256Swatch:
        """
        Get a swatch with given number of colors
        """
        index = num_colors - self.min_colors
        return self.swatches[index]

    def get_hex_swatch(self, num_colors: int) -> RGBHexSwatch:
        """
        Get a swatch with given number of colors in hex
        """
        swatch = self.get_swatch(num_colors)
        return RGB256Swatch_to_RGBHexSwatch(swatch)

    @cached_property
    def colormap(self) -> PaletteInterpolatedMap:
        """
        Return a colormap representation of the palette
        """
        return PaletteInterpolatedMap(self)


def HX(n: int) -> str:
    """
    Conver 8-Bit int to two character HEX (uppercase)

    Should be in the range [0, 255]
    """
    return f"{hex(n)[2:]:>02}".upper()


def RGB256Color_to_RGBHexColor(color: RGB256Color) -> RGBHexColor:
    """
    Covert 256Color to HexColor
    """
    return "#" + "".join(HX(i) for i in color)


def RGB256Swatch_to_RGBHexSwatch(swatch: RGB256Swatch) -> RGBHexSwatch:
    """
    Covert 256Swatch to HexSwatch
    """
    return [RGB256Color_to_RGBHexColor(color) for color in swatch]
