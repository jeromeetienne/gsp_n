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


# =============================================================================
# Transform
# =============================================================================
class TransformChain:
    """Chain of transformations to apply to data."""

    def __init__(self) -> None:
        self.links: list[TransformLink] = []
        """Ordered list of links defining the transform."""

    def add(self, link: TransformLink) -> None:
        """Add a TransformLink to the chain."""
        self.links.append(link)

    def clear(self) -> None:
        """Clear all TransformLinks from the chain."""
        self.links.clear()

    def remove(self, link: TransformLink) -> None:
        """Remove a TransformLink from the chain."""
        self.links.remove(link)

    def to_buffer(self) -> Buffer:
        """Compute the transform and return a Buffer with the result."""

        # TODO to hardcode in BufferType.uint8 is crap.
        # - i think the transform should know its output type, from the start. Thus a lot of checks can be done earlier.
        # - maybe support BufferType.Any
        #   - with BufferType.isAlias(buffer_type: BufferType) method which return true IIF buffer_type === BufferType.Any

        # Create a new Buffer to hold the transformed data
        buffer = Buffer(0, BufferType.uint8)

        # Apply each link in the chain
        for link in self.links:
            buffer = link.apply(buffer)

        return buffer
