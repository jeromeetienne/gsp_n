from ..core.visual_base import VisualBase
from ..math.mat4 import Mat4
from ..types.types import TransBuf

class Pixels(VisualBase):
    def __init__(self, positions: TransBuf, colors: TransBuf, groups: TransBuf):
        super().__init__()

        self.positions = positions
        self.colors = colors
        self.groups = groups
        self.model_matrix = Mat4()

    # =============================================================================
    # Model Matrix
    # =============================================================================

    def set_model_matrix(self, model_matrix: Mat4):
        self.model_matrix = model_matrix

    def get_model_matrix(self) -> Mat4:
        return self.model_matrix