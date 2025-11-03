# stdlib imports
from typing import Any

# local imports
from ..utils.uuid_utils import UuidUtils


class Viewport:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.uuid: str = UuidUtils.generate_uuid()
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.userData: dict[str, Any] = {}
