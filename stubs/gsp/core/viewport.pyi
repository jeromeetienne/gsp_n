from ..utils.uuid_utils import UuidUtils as UuidUtils
from typing import Any

class Viewport:
    uuid: str
    x: int
    y: int
    width: int
    height: int
    userData: dict[str, Any]
    def __init__(self, x: int, y: int, width: int, height: int) -> None: ...
