import numpy as np
from ..types.group import Groups as Groups

class GroupUtils:
    @staticmethod
    def is_instance_of_groups(groups: Groups) -> bool: ...
    @staticmethod
    def compute_indices_per_group(vertices_numpy: np.ndarray, groups: object) -> tuple[int, list[list[int]]]: ...
