from ..core.visual_base import VisualBase
from ..types.transbuf import TransBuf
from ..types.group import Groups


class Points(VisualBase):
    def __init__(self, positions: TransBuf, sizes: TransBuf, face_colors: TransBuf, edge_colors: TransBuf, edge_widths: TransBuf, groups: Groups):
        super().__init__()

        self.positions: TransBuf = positions
        self.sizes: TransBuf = sizes
        self.face_colors: TransBuf = face_colors
        self.edge_colors: TransBuf = edge_colors
        self.edge_widths: TransBuf = edge_widths
        self.groups: Groups = groups
