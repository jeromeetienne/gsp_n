from ..core.visual_base import VisualBase
from ..math.mat4 import Mat4
from ..types.transbuf import TransBuf

class Points(VisualBase):
    # TODO 
    def __init__(self, positions: TransBuf, sizes: TransBuf, face_colors: TransBuf, edge_colors: TransBuf, edge_widths: TransBuf, groups: TransBuf):
        super().__init__()

        self.positions = positions
        self.sizes = sizes
        self.face_colors = face_colors
        self.edge_colors = edge_colors
        self.edge_widths = edge_widths
        self.groups = groups
        self.model_matrix = Mat4()

    # =============================================================================
    # Model Matrix
    # =============================================================================

    def set_model_matrix(self, model_matrix: Mat4):
        self.model_matrix = model_matrix

    def get_model_matrix(self) -> Mat4:
        return self.model_matrix