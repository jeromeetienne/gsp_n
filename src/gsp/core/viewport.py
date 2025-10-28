# pip imports
import uuid

# local imports
from .uuid_utils import UuidUtils

class Viewport:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.uuid = UuidUtils.generate_uuid()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.userData = {}  
