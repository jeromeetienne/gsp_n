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
