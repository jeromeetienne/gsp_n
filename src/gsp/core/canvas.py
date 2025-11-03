# stdlib imports
from typing import Any

# local imports
from ..utils.uuid_utils import UuidUtils


class Canvas:
    def __init__(self, width: int, height: int, dpi: float):
        self.uuid: str = UuidUtils.generate_uuid()
        self.width: int = width
        self.height: int = height
        self.dpi: float = dpi
        self.userData: dict[str, Any] = {}

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def get_dpi(self) -> float:
        return self.dpi
