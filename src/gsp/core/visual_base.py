# pip imports
import uuid

# local imports
from .uuid_utils import UuidUtils

class VisualBase:
    def __init__(self):
        self.uuid = UuidUtils.generate_uuid()
        self.userData = {}      