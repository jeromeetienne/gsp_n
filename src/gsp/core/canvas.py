# pip imports
import uuid

# local imports
from .viewport import Viewport
from .uuid_utils import UuidUtils


class Canvas:
    def __init__(self, width: int, height: int, dpi: float):
        self.uuid = UuidUtils.generate_uuid()
        self.width = width
        self.height = height
        self.dpi = dpi
        self.userData = {}

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def get_dpi(self) -> float:
        return self.dpi
