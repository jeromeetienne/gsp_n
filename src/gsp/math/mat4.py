# pip imports
import numpy as np

class Mat4:
    """matrix 4x4 class, row major order"""
    def __init__(self, data: list[list[int|float]] | None = None):
        if data is None:
            data = [[0, 0, 0, 0] for _ in range(4)]
        self.data: np.ndarray = np.array(data, dtype=np.float32)

    @staticmethod
    def from_numpy(data: np.ndarray) -> "Mat4":
        return Mat4(data.tolist())