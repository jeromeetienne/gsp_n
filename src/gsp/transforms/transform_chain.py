# local imports
from ..types import BufferType, Buffer
from .transform_link import TransformLink


# =============================================================================
# Transform
# =============================================================================
class TransformChain:
    """Chain of transformations to apply to data."""

    def __init__(self) -> None:
        self.links: list[TransformLink] = []
        """Ordered list of links defining the transform."""

    # =============================================================================
    # .add/.remove/.clear the links
    # =============================================================================

    def add(self, link: TransformLink) -> None:
        """Add a TransformLink to the chain."""
        self.links.append(link)

    def clear(self) -> None:
        """Clear all TransformLinks from the chain."""
        self.links.clear()

    def remove(self, link: TransformLink) -> None:
        """Remove a TransformLink from the chain."""
        self.links.remove(link)

    # =============================================================================
    # .run()
    # =============================================================================

    def run(self) -> Buffer:
        """Compute the transform and return a Buffer with the result."""

        # Create a new Buffer to hold the transformed data
        buffer = None

        # Apply each link in the chain
        for link in self.links:
            buffer = link.apply(buffer)

        # Sanity check the output buffer
        assert buffer is not None, "TransformChain.to_buffer: No buffer produced by the transform chain."

        # Return the final buffer
        return buffer
