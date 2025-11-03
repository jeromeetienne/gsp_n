from ..types import Buffer as Buffer, BufferType as BufferType

class TransformLink:
    def apply(self, buffer: Buffer) -> Buffer: ...
