from .buffer import Buffer as Buffer
from .transbuf import TransBuf as TransBuf

class TransBufUtils:
    @staticmethod
    def to_buffer(trans_buf: TransBuf) -> Buffer: ...
