# stdlib imports
from typing import Any

# local imports
from ..types.transbuf import TransBuf
from ..utils.uuid_utils import UuidUtils


class Camera:
    def __init__(self, view_matrix: TransBuf, projection_matrix: TransBuf):
        self.uuid: str = UuidUtils.generate_uuid()
        self.view_matrix: TransBuf = view_matrix
        self.projection_matrix: TransBuf = projection_matrix
        self.userData: dict[str, Any] = {}

    def set_view_matrix(self, view_matrix: TransBuf):
        self.view_matrix = view_matrix

    def get_view_matrix(self) -> TransBuf:
        return self.view_matrix

    def set_projection_matrix(self, projection_matrix: TransBuf):
        self.projection_matrix = projection_matrix

    def get_projection_matrix(self) -> TransBuf:
        return self.projection_matrix
