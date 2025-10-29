from ..core.visual_base import VisualBase
from ..types.transbuf import TransBuf


class Pixels(VisualBase):
    def __init__(self, positions: TransBuf, colors: TransBuf, groups: TransBuf):
        super().__init__()

        self.positions = positions
        self.colors = colors
        self.groups = groups
