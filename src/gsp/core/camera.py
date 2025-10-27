# pip imports
import uuid

# local imports
from ..math.mat4 import Mat4

class Camera:
    def __init__(self, view_matrix: Mat4 | None = None, projection_matrix: Mat4 | None = None):
        self.uuid = str(uuid.uuid4())
        self.view_matrix = view_matrix if view_matrix is not None else Mat4()
        self.projection_matrix = projection_matrix if projection_matrix is not None else Mat4()

    def set_view_matrix(self, view_matrix: Mat4):
        self.view_matrix = view_matrix

    def get_view_matrix(self) -> Mat4:
        return self.view_matrix

    def set_projection_matrix(self, projection_matrix: Mat4):
        self.projection_matrix = projection_matrix

    def get_projection_matrix(self) -> Mat4:
        return self.projection_matrix