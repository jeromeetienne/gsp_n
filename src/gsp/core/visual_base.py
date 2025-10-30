# stdlib imports
from typing import Any

# local imports
from .uuid_utils import UuidUtils


class VisualBase:
    def __init__(self):
        self.uuid: str = UuidUtils.generate_uuid()
        self.userData: dict[str, Any] = {}
