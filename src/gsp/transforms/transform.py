from typing import Literal
from gsp.types import BufferType, Buffer
import numpy
import requests
import os
import imageio.v3 


class TransformLink:
    """Base class for a link in a Transform chain."""

    def apply(self, buffer: Buffer) -> Buffer:
        """Apply the transformation to the given buffer and return a new buffer."""
        raise NotImplementedError("TransformLink.apply is not implemented yet.")

class Transform:
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
        # Create a new Buffer to hold the transformed data
        buffer = Buffer(0, BufferType.uint8)

        # Apply each link in the chain
        for link in self.links:
            buffer = link.apply(buffer)

        return buffer

# =============================================================================
# 
# =============================================================================

class TransformDataSource(TransformLink):
    """Load data from a URI into a Buffer. previous buffer is ignored."""

    def __init__(self, uri: str, buffer_type: BufferType) -> None:
        self._uri = uri
        self._buffer_type = buffer_type

    def apply(self,_buffer: Buffer) -> Buffer:
        item_size = BufferType.get_item_size(self._buffer_type)
        
        is_image = os.path.splitext(self._uri)[1].lower() in [".png", ".jpg", ".jpeg", ".bmp", ".tiff"]
        if is_image:
            # If the URI points to an image, use imageio to load it

            # Load image data
            image_data = imageio.v3.imread(self._uri)

            # sanity check
            assert image_data.nbytes % item_size == 0, f"Image data size {image_data.nbytes} is not aligned with buffer type item size {item_size}"

            # Build a new buffer
            count = image_data.nbytes // item_size
            new_buffer = Buffer(count, self._buffer_type)
            new_buffer.set_data(image_data.tobytes(), 0, count)
            return new_buffer
        else:
            # Load data from URI
            response = requests.get(self._uri)
            response.raise_for_status()
            content = response.content
            
            # sanity check
            assert len(content) % item_size == 0, f"Data size {len(content)} is not a multiple of item size {item_size} for buffer type {self._buffer_type}"

            count = len(content) // item_size
            new_buffer = Buffer(count, self._buffer_type)
            new_buffer.set_data(content, 0, count)
            return new_buffer


TransformAccessorFieldName = Literal['r','g','b','a','x','y','z','w']
class TransformAccessor(TransformLink):
    """Access a subset of the input Buffer."""

    def __init__(self, field_name: TransformAccessorFieldName) -> None:
        self._field_name = field_name

    def apply(self, buffer: Buffer) -> Buffer:
        # Map field names to indices
        field_to_index = {
            'r': 0, 'g': 1, 'b': 2, 'a': 3,
            'x': 0, 'y': 1, 'z': 2, 'w': 3
        }
        index = field_to_index[self._field_name]
        item_size = BufferType.get_item_size(buffer.get_type())

        # sanity check
        assert buffer.get_count() % 4 == 0, f"Input buffer count must be a multiple of 4"

        # Create a new buffer for the accessed field
        new_count = buffer.get_count() // 4
        new_buffer = Buffer(new_count, buffer.get_type())
        
        return new_buffer
