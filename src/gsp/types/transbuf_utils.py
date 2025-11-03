# stdlib imports
import numpy as np

# local imports
from .transbuf import TransBuf
from .buffer import Buffer


class TransBufUtils:
    @staticmethod
    def transbuf_to_buffer(trans_buf: TransBuf) -> Buffer:
        """Convert a TransBuf to a Buffer."""
        if isinstance(trans_buf, Buffer):
            return trans_buf
        elif isinstance(trans_buf, TransBuf):
            raise NotImplementedError("TransBuf to Buffer conversion is not implemented yet.")
        else:
            raise ValueError(f"Unsupported type for transbuf_to_buffer")
