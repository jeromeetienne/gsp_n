from ..utils.uuid_utils import UuidUtils as UuidUtils
from typing import Any

class VisualBase:
    uuid: str
    userData: dict[str, Any]
    def __init__(self) -> None: ...
