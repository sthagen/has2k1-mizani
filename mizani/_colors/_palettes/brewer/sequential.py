from .. import palette
from .._palette import PaletteKind as pk

__all__ = [
    "Blues",
    "BuGn",
    "BuPu",
    "GnBu",
    "Greens",
    "Greys",
    "Oranges",
    "OrRd",
    "PuBu",
    "PuBuGn",
    "PuRd",
    "Purples",
    "RdPu",
    "Reds",
    "YlGn",
    "YlGnBu",
    "YlOrBr",
    "YlOrRd",
]

Blues = palette(
    name="Blues",
    swatches=[
        [(222, 235, 247), (158, 202, 225), (49, 130, 189)],
        [(239, 243, 255), (189, 215, 231), (107, 174, 214), (33, 113, 181)],
        [
            (239, 243, 255),
            (189, 215, 231),
            (107, 174, 214),
            (49, 130, 189),
            (8, 81, 156),
        ],
        [
            (239, 243, 255),
            (198, 219, 239),
            (158, 202, 225),
            (107, 174, 214),
            (49, 130, 189),
            (8, 81, 156),
        ],
        [
            (239, 243, 255),
            (198, 219, 239),
            (158, 202, 225),
            (107, 174, 214),
            (66, 146, 198),
            (33, 113, 181),
            (8, 69, 148),
        ],
        [
            (247, 251, 255),
            (222, 235, 247),
            (198, 219, 239),
            (158, 202, 225),
            (107, 174, 214),
            (66, 146, 198),
            (33, 113, 181),
            (8, 69, 148),
        ],
        [
            (247, 251, 255),
            (222, 235, 247),
            (198, 219, 239),
            (158, 202, 225),
            (107, 174, 214),
            (66, 146, 198),
            (33, 113, 181),
            (8, 81, 156),
            (8, 48, 107),
        ],
    ],
    kind=pk.sequential,
)

BuGn = palette(
    name="BuGn",
    swatches=[
        [(229, 245, 249), (153, 216, 201), (44, 162, 95)],
        [(237, 248, 251), (178, 226, 226), (102, 194, 164), (35, 139, 69)],
        [
            (237, 248, 251),
            (178, 226, 226),
            (102, 194, 164),
            (44, 162, 95),
            (0, 109, 44),
        ],
        [
            (237, 248, 251),
            (204, 236, 230),
            (153, 216, 201),
            (102, 194, 164),
            (44, 162, 95),
            (0, 109, 44),
        ],
        [
            (237, 248, 251),
            (204, 236, 230),
            (153, 216, 201),
            (102, 194, 164),
            (65, 174, 118),
            (35, 139, 69),
            (0, 88, 36),
        ],
        [
            (247, 252, 253),
            (229, 245, 249),
            (204, 236, 230),
            (153, 216, 201),
            (102, 194, 164),
            (65, 174, 118),
            (35, 139, 69),
            (0, 88, 36),
        ],
        [
            (247, 252, 253),
            (229, 245, 249),
            (204, 236, 230),
            (153, 216, 201),
            (102, 194, 164),
            (65, 174, 118),
            (35, 139, 69),
            (0, 109, 44),
            (0, 68, 27),
        ],
    ],
    kind=pk.sequential,
)

BuPu = palette(
    name="BuPu",
    swatches=[
        [(224, 236, 244), (158, 188, 218), (136, 86, 167)],
        [(237, 248, 251), (179, 205, 227), (140, 150, 198), (136, 65, 157)],
        [
            (237, 248, 251),
            (179, 205, 227),
            (140, 150, 198),
            (136, 86, 167),
            (129, 15, 124),
        ],
        [
            (237, 248, 251),
            (191, 211, 230),
            (158, 188, 218),
            (140, 150, 198),
            (136, 86, 167),
            (129, 15, 124),
        ],
        [
            (237, 248, 251),
            (191, 211, 230),
            (158, 188, 218),
            (140, 150, 198),
            (140, 107, 177),
            (136, 65, 157),
            (110, 1, 107),
        ],
        [
            (247, 252, 253),
            (224, 236, 244),
            (191, 211, 230),
            (158, 188, 218),
            (140, 150, 198),
            (140, 107, 177),
            (136, 65, 157),
            (110, 1, 107),
        ],
        [
            (247, 252, 253),
            (224, 236, 244),
            (191, 211, 230),
            (158, 188, 218),
            (140, 150, 198),
            (140, 107, 177),
            (136, 65, 157),
            (129, 15, 124),
            (77, 0, 75),
        ],
    ],
    kind=pk.sequential,
)

GnBu = palette(
    name="GnBu",
    swatches=[
        [(224, 243, 219), (168, 221, 181), (67, 162, 202)],
        [(240, 249, 232), (186, 228, 188), (123, 204, 196), (43, 140, 190)],
        [
            (240, 249, 232),
            (186, 228, 188),
            (123, 204, 196),
            (67, 162, 202),
            (8, 104, 172),
        ],
        [
            (240, 249, 232),
            (204, 235, 197),
            (168, 221, 181),
            (123, 204, 196),
            (67, 162, 202),
            (8, 104, 172),
        ],
        [
            (240, 249, 232),
            (204, 235, 197),
            (168, 221, 181),
            (123, 204, 196),
            (78, 179, 211),
            (43, 140, 190),
            (8, 88, 158),
        ],
        [
            (247, 252, 240),
            (224, 243, 219),
            (204, 235, 197),
            (168, 221, 181),
            (123, 204, 196),
            (78, 179, 211),
            (43, 140, 190),
            (8, 88, 158),
        ],
        [
            (247, 252, 240),
            (224, 243, 219),
            (204, 235, 197),
            (168, 221, 181),
            (123, 204, 196),
            (78, 179, 211),
            (43, 140, 190),
            (8, 104, 172),
            (8, 64, 129),
        ],
    ],
    kind=pk.sequential,
)

Greens = palette(
    name="Greens",
    swatches=[
        [(229, 245, 224), (161, 217, 155), (49, 163, 84)],
        [(237, 248, 233), (186, 228, 179), (116, 196, 118), (35, 139, 69)],
        [
            (237, 248, 233),
            (186, 228, 179),
            (116, 196, 118),
            (49, 163, 84),
            (0, 109, 44),
        ],
        [
            (237, 248, 233),
            (199, 233, 192),
            (161, 217, 155),
            (116, 196, 118),
            (49, 163, 84),
            (0, 109, 44),
        ],
        [
            (237, 248, 233),
            (199, 233, 192),
            (161, 217, 155),
            (116, 196, 118),
            (65, 171, 93),
            (35, 139, 69),
            (0, 90, 50),
        ],
        [
            (247, 252, 245),
            (229, 245, 224),
            (199, 233, 192),
            (161, 217, 155),
            (116, 196, 118),
            (65, 171, 93),
            (35, 139, 69),
            (0, 90, 50),
        ],
        [
            (247, 252, 245),
            (229, 245, 224),
            (199, 233, 192),
            (161, 217, 155),
            (116, 196, 118),
            (65, 171, 93),
            (35, 139, 69),
            (0, 109, 44),
            (0, 68, 27),
        ],
    ],
    kind=pk.sequential,
)

Greys = palette(
    name="Greys",
    swatches=[
        [(240, 240, 240), (189, 189, 189), (99, 99, 99)],
        [(247, 247, 247), (204, 204, 204), (150, 150, 150), (82, 82, 82)],
        [
            (247, 247, 247),
            (204, 204, 204),
            (150, 150, 150),
            (99, 99, 99),
            (37, 37, 37),
        ],
        [
            (247, 247, 247),
            (217, 217, 217),
            (189, 189, 189),
            (150, 150, 150),
            (99, 99, 99),
            (37, 37, 37),
        ],
        [
            (247, 247, 247),
            (217, 217, 217),
            (189, 189, 189),
            (150, 150, 150),
            (115, 115, 115),
            (82, 82, 82),
            (37, 37, 37),
        ],
        [
            (255, 255, 255),
            (240, 240, 240),
            (217, 217, 217),
            (189, 189, 189),
            (150, 150, 150),
            (115, 115, 115),
            (82, 82, 82),
            (37, 37, 37),
        ],
        [
            (255, 255, 255),
            (240, 240, 240),
            (217, 217, 217),
            (189, 189, 189),
            (150, 150, 150),
            (115, 115, 115),
            (82, 82, 82),
            (37, 37, 37),
            (0, 0, 0),
        ],
    ],
    kind=pk.sequential,
)

Oranges = palette(
    name="Oranges",
    swatches=[
        [(254, 230, 206), (253, 174, 107), (230, 85, 13)],
        [(254, 237, 222), (253, 190, 133), (253, 141, 60), (217, 71, 1)],
        [
            (254, 237, 222),
            (253, 190, 133),
            (253, 141, 60),
            (230, 85, 13),
            (166, 54, 3),
        ],
        [
            (254, 237, 222),
            (253, 208, 162),
            (253, 174, 107),
            (253, 141, 60),
            (230, 85, 13),
            (166, 54, 3),
        ],
        [
            (254, 237, 222),
            (253, 208, 162),
            (253, 174, 107),
            (253, 141, 60),
            (241, 105, 19),
            (217, 72, 1),
            (140, 45, 4),
        ],
        [
            (255, 245, 235),
            (254, 230, 206),
            (253, 208, 162),
            (253, 174, 107),
            (253, 141, 60),
            (241, 105, 19),
            (217, 72, 1),
            (140, 45, 4),
        ],
        [
            (255, 245, 235),
            (254, 230, 206),
            (253, 208, 162),
            (253, 174, 107),
            (253, 141, 60),
            (241, 105, 19),
            (217, 72, 1),
            (166, 54, 3),
            (127, 39, 4),
        ],
    ],
    kind=pk.sequential,
)

OrRd = palette(
    name="OrRd",
    swatches=[
        [(254, 232, 200), (253, 187, 132), (227, 74, 51)],
        [(254, 240, 217), (253, 204, 138), (252, 141, 89), (215, 48, 31)],
        [
            (254, 240, 217),
            (253, 204, 138),
            (252, 141, 89),
            (227, 74, 51),
            (179, 0, 0),
        ],
        [
            (254, 240, 217),
            (253, 212, 158),
            (253, 187, 132),
            (252, 141, 89),
            (227, 74, 51),
            (179, 0, 0),
        ],
        [
            (254, 240, 217),
            (253, 212, 158),
            (253, 187, 132),
            (252, 141, 89),
            (239, 101, 72),
            (215, 48, 31),
            (153, 0, 0),
        ],
        [
            (255, 247, 236),
            (254, 232, 200),
            (253, 212, 158),
            (253, 187, 132),
            (252, 141, 89),
            (239, 101, 72),
            (215, 48, 31),
            (153, 0, 0),
        ],
        [
            (255, 247, 236),
            (254, 232, 200),
            (253, 212, 158),
            (253, 187, 132),
            (252, 141, 89),
            (239, 101, 72),
            (215, 48, 31),
            (179, 0, 0),
            (127, 0, 0),
        ],
    ],
    kind=pk.sequential,
)

PuBu = palette(
    name="PuBu",
    swatches=[
        [(236, 231, 242), (166, 189, 219), (43, 140, 190)],
        [(241, 238, 246), (189, 201, 225), (116, 169, 207), (5, 112, 176)],
        [
            (241, 238, 246),
            (189, 201, 225),
            (116, 169, 207),
            (43, 140, 190),
            (4, 90, 141),
        ],
        [
            (241, 238, 246),
            (208, 209, 230),
            (166, 189, 219),
            (116, 169, 207),
            (43, 140, 190),
            (4, 90, 141),
        ],
        [
            (241, 238, 246),
            (208, 209, 230),
            (166, 189, 219),
            (116, 169, 207),
            (54, 144, 192),
            (5, 112, 176),
            (3, 78, 123),
        ],
        [
            (255, 247, 251),
            (236, 231, 242),
            (208, 209, 230),
            (166, 189, 219),
            (116, 169, 207),
            (54, 144, 192),
            (5, 112, 176),
            (3, 78, 123),
        ],
        [
            (255, 247, 251),
            (236, 231, 242),
            (208, 209, 230),
            (166, 189, 219),
            (116, 169, 207),
            (54, 144, 192),
            (5, 112, 176),
            (4, 90, 141),
            (2, 56, 88),
        ],
    ],
    kind=pk.sequential,
)

PuBuGn = palette(
    name="PuBuGn",
    swatches=[
        [(236, 226, 240), (166, 189, 219), (28, 144, 153)],
        [(246, 239, 247), (189, 201, 225), (103, 169, 207), (2, 129, 138)],
        [
            (246, 239, 247),
            (189, 201, 225),
            (103, 169, 207),
            (28, 144, 153),
            (1, 108, 89),
        ],
        [
            (246, 239, 247),
            (208, 209, 230),
            (166, 189, 219),
            (103, 169, 207),
            (28, 144, 153),
            (1, 108, 89),
        ],
        [
            (246, 239, 247),
            (208, 209, 230),
            (166, 189, 219),
            (103, 169, 207),
            (54, 144, 192),
            (2, 129, 138),
            (1, 100, 80),
        ],
        [
            (255, 247, 251),
            (236, 226, 240),
            (208, 209, 230),
            (166, 189, 219),
            (103, 169, 207),
            (54, 144, 192),
            (2, 129, 138),
            (1, 100, 80),
        ],
        [
            (255, 247, 251),
            (236, 226, 240),
            (208, 209, 230),
            (166, 189, 219),
            (103, 169, 207),
            (54, 144, 192),
            (2, 129, 138),
            (1, 108, 89),
            (1, 70, 54),
        ],
    ],
    kind=pk.sequential,
)

PuRd = palette(
    name="PuRd",
    swatches=[
        [(231, 225, 239), (201, 148, 199), (221, 28, 119)],
        [(241, 238, 246), (215, 181, 216), (223, 101, 176), (206, 18, 86)],
        [
            (241, 238, 246),
            (215, 181, 216),
            (223, 101, 176),
            (221, 28, 119),
            (152, 0, 67),
        ],
        [
            (241, 238, 246),
            (212, 185, 218),
            (201, 148, 199),
            (223, 101, 176),
            (221, 28, 119),
            (152, 0, 67),
        ],
        [
            (241, 238, 246),
            (212, 185, 218),
            (201, 148, 199),
            (223, 101, 176),
            (231, 41, 138),
            (206, 18, 86),
            (145, 0, 63),
        ],
        [
            (247, 244, 249),
            (231, 225, 239),
            (212, 185, 218),
            (201, 148, 199),
            (223, 101, 176),
            (231, 41, 138),
            (206, 18, 86),
            (145, 0, 63),
        ],
        [
            (247, 244, 249),
            (231, 225, 239),
            (212, 185, 218),
            (201, 148, 199),
            (223, 101, 176),
            (231, 41, 138),
            (206, 18, 86),
            (152, 0, 67),
            (103, 0, 31),
        ],
    ],
    kind=pk.sequential,
)

Purples = palette(
    name="Purples",
    swatches=[
        [(239, 237, 245), (188, 189, 220), (117, 107, 177)],
        [(242, 240, 247), (203, 201, 226), (158, 154, 200), (106, 81, 163)],
        [
            (242, 240, 247),
            (203, 201, 226),
            (158, 154, 200),
            (117, 107, 177),
            (84, 39, 143),
        ],
        [
            (242, 240, 247),
            (218, 218, 235),
            (188, 189, 220),
            (158, 154, 200),
            (117, 107, 177),
            (84, 39, 143),
        ],
        [
            (242, 240, 247),
            (218, 218, 235),
            (188, 189, 220),
            (158, 154, 200),
            (128, 125, 186),
            (106, 81, 163),
            (74, 20, 134),
        ],
        [
            (252, 251, 253),
            (239, 237, 245),
            (218, 218, 235),
            (188, 189, 220),
            (158, 154, 200),
            (128, 125, 186),
            (106, 81, 163),
            (74, 20, 134),
        ],
        [
            (252, 251, 253),
            (239, 237, 245),
            (218, 218, 235),
            (188, 189, 220),
            (158, 154, 200),
            (128, 125, 186),
            (106, 81, 163),
            (84, 39, 143),
            (63, 0, 125),
        ],
    ],
    kind=pk.sequential,
)

RdPu = palette(
    name="RdPu",
    swatches=[
        [(253, 224, 221), (250, 159, 181), (197, 27, 138)],
        [(254, 235, 226), (251, 180, 185), (247, 104, 161), (174, 1, 126)],
        [
            (254, 235, 226),
            (251, 180, 185),
            (247, 104, 161),
            (197, 27, 138),
            (122, 1, 119),
        ],
        [
            (254, 235, 226),
            (252, 197, 192),
            (250, 159, 181),
            (247, 104, 161),
            (197, 27, 138),
            (122, 1, 119),
        ],
        [
            (254, 235, 226),
            (252, 197, 192),
            (250, 159, 181),
            (247, 104, 161),
            (221, 52, 151),
            (174, 1, 126),
            (122, 1, 119),
        ],
        [
            (255, 247, 243),
            (253, 224, 221),
            (252, 197, 192),
            (250, 159, 181),
            (247, 104, 161),
            (221, 52, 151),
            (174, 1, 126),
            (122, 1, 119),
        ],
        [
            (255, 247, 243),
            (253, 224, 221),
            (252, 197, 192),
            (250, 159, 181),
            (247, 104, 161),
            (221, 52, 151),
            (174, 1, 126),
            (122, 1, 119),
            (73, 0, 106),
        ],
    ],
    kind=pk.sequential,
)

Reds = palette(
    name="Reds",
    swatches=[
        [(254, 224, 210), (252, 146, 114), (222, 45, 38)],
        [(254, 229, 217), (252, 174, 145), (251, 106, 74), (203, 24, 29)],
        [
            (254, 229, 217),
            (252, 174, 145),
            (251, 106, 74),
            (222, 45, 38),
            (165, 15, 21),
        ],
        [
            (254, 229, 217),
            (252, 187, 161),
            (252, 146, 114),
            (251, 106, 74),
            (222, 45, 38),
            (165, 15, 21),
        ],
        [
            (254, 229, 217),
            (252, 187, 161),
            (252, 146, 114),
            (251, 106, 74),
            (239, 59, 44),
            (203, 24, 29),
            (153, 0, 13),
        ],
        [
            (255, 245, 240),
            (254, 224, 210),
            (252, 187, 161),
            (252, 146, 114),
            (251, 106, 74),
            (239, 59, 44),
            (203, 24, 29),
            (153, 0, 13),
        ],
        [
            (255, 245, 240),
            (254, 224, 210),
            (252, 187, 161),
            (252, 146, 114),
            (251, 106, 74),
            (239, 59, 44),
            (203, 24, 29),
            (165, 15, 21),
            (103, 0, 13),
        ],
    ],
    kind=pk.sequential,
)

YlGn = palette(
    name="YlGn",
    swatches=[
        [(247, 252, 185), (173, 221, 142), (49, 163, 84)],
        [(255, 255, 204), (194, 230, 153), (120, 198, 121), (35, 132, 67)],
        [
            (255, 255, 204),
            (194, 230, 153),
            (120, 198, 121),
            (49, 163, 84),
            (0, 104, 55),
        ],
        [
            (255, 255, 204),
            (217, 240, 163),
            (173, 221, 142),
            (120, 198, 121),
            (49, 163, 84),
            (0, 104, 55),
        ],
        [
            (255, 255, 204),
            (217, 240, 163),
            (173, 221, 142),
            (120, 198, 121),
            (65, 171, 93),
            (35, 132, 67),
            (0, 90, 50),
        ],
        [
            (255, 255, 229),
            (247, 252, 185),
            (217, 240, 163),
            (173, 221, 142),
            (120, 198, 121),
            (65, 171, 93),
            (35, 132, 67),
            (0, 90, 50),
        ],
        [
            (255, 255, 229),
            (247, 252, 185),
            (217, 240, 163),
            (173, 221, 142),
            (120, 198, 121),
            (65, 171, 93),
            (35, 132, 67),
            (0, 104, 55),
            (0, 69, 41),
        ],
    ],
    kind=pk.sequential,
)

YlGnBu = palette(
    name="YlGnBu",
    swatches=[
        [(237, 248, 177), (127, 205, 187), (44, 127, 184)],
        [(255, 255, 204), (161, 218, 180), (65, 182, 196), (34, 94, 168)],
        [
            (255, 255, 204),
            (161, 218, 180),
            (65, 182, 196),
            (44, 127, 184),
            (37, 52, 148),
        ],
        [
            (255, 255, 204),
            (199, 233, 180),
            (127, 205, 187),
            (65, 182, 196),
            (44, 127, 184),
            (37, 52, 148),
        ],
        [
            (255, 255, 204),
            (199, 233, 180),
            (127, 205, 187),
            (65, 182, 196),
            (29, 145, 192),
            (34, 94, 168),
            (12, 44, 132),
        ],
        [
            (255, 255, 217),
            (237, 248, 177),
            (199, 233, 180),
            (127, 205, 187),
            (65, 182, 196),
            (29, 145, 192),
            (34, 94, 168),
            (12, 44, 132),
        ],
        [
            (255, 255, 217),
            (237, 248, 177),
            (199, 233, 180),
            (127, 205, 187),
            (65, 182, 196),
            (29, 145, 192),
            (34, 94, 168),
            (37, 52, 148),
            (8, 29, 88),
        ],
    ],
    kind=pk.sequential,
)

YlOrBr = palette(
    name="YlOrBr",
    swatches=[
        [(255, 247, 188), (254, 196, 79), (217, 95, 14)],
        [(255, 255, 212), (254, 217, 142), (254, 153, 41), (204, 76, 2)],
        [
            (255, 255, 212),
            (254, 217, 142),
            (254, 153, 41),
            (217, 95, 14),
            (153, 52, 4),
        ],
        [
            (255, 255, 212),
            (254, 227, 145),
            (254, 196, 79),
            (254, 153, 41),
            (217, 95, 14),
            (153, 52, 4),
        ],
        [
            (255, 255, 212),
            (254, 227, 145),
            (254, 196, 79),
            (254, 153, 41),
            (236, 112, 20),
            (204, 76, 2),
            (140, 45, 4),
        ],
        [
            (255, 255, 229),
            (255, 247, 188),
            (254, 227, 145),
            (254, 196, 79),
            (254, 153, 41),
            (236, 112, 20),
            (204, 76, 2),
            (140, 45, 4),
        ],
        [
            (255, 255, 229),
            (255, 247, 188),
            (254, 227, 145),
            (254, 196, 79),
            (254, 153, 41),
            (236, 112, 20),
            (204, 76, 2),
            (153, 52, 4),
            (102, 37, 6),
        ],
    ],
    kind=pk.sequential,
)

YlOrRd = palette(
    name="YlOrRd",
    swatches=[
        [(255, 237, 160), (254, 178, 76), (240, 59, 32)],
        [(255, 255, 178), (254, 204, 92), (253, 141, 60), (227, 26, 28)],
        [
            (255, 255, 178),
            (254, 204, 92),
            (253, 141, 60),
            (240, 59, 32),
            (189, 0, 38),
        ],
        [
            (255, 255, 178),
            (254, 217, 118),
            (254, 178, 76),
            (253, 141, 60),
            (240, 59, 32),
            (189, 0, 38),
        ],
        [
            (255, 255, 178),
            (254, 217, 118),
            (254, 178, 76),
            (253, 141, 60),
            (252, 78, 42),
            (227, 26, 28),
            (177, 0, 38),
        ],
        [
            (255, 255, 204),
            (255, 237, 160),
            (254, 217, 118),
            (254, 178, 76),
            (253, 141, 60),
            (252, 78, 42),
            (227, 26, 28),
            (177, 0, 38),
        ],
        [
            (255, 255, 204),
            (255, 237, 160),
            (254, 217, 118),
            (254, 178, 76),
            (253, 141, 60),
            (252, 78, 42),
            (227, 26, 28),
            (189, 0, 38),
            (128, 0, 38),
        ],
    ],
    kind=pk.sequential,
)
