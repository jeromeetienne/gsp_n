# local imports
from ..types import BufferType, Buffer


# =============================================================================
# TransformLink
# =============================================================================
class TransformLink:
    """Base class for a link in a Transform chain."""

    def apply(self, buffer: Buffer) -> Buffer:
        """Apply the transformation to the given buffer and return a new buffer."""
        raise NotImplementedError("TransformLink.apply is not implemented yet.")
