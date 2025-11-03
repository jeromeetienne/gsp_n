# stdlib imports
import numpy as np

# local imports
from ..types.group import Groups


class GroupUtils:

    @staticmethod
    def is_instance_of_groups(groups: Groups) -> bool:
        """Check if the object is an instance of groups.
        groups can be:
        - int
        - list[int]
        - list[list[int]]

        """

        if isinstance(groups, int):
            return True
        elif isinstance(groups, list) and all(isinstance(int_value, int) for int_value in groups):
            return True
        elif isinstance(groups, list) and all(isinstance(group, list) for group in groups) and all(isinstance(int_value, int) for int_list in groups for int_value in int_list):  # type: ignore[union-attr]
            return True
        else:
            return False

    @staticmethod
    def compute_indices_per_group(vertices_numpy: np.ndarray, groups: object) -> tuple[int, list[list[int]]]:
        """Compute indices_per_group for groups depending on the type of groups"""

        if isinstance(groups, int):
            # In this case, groups buffer contains only the number of groups
            # indices per groups = [list of vertex indices for each group]
            # if group_count = 2, split the vertices in two halves
            # if group_count = 3, split the vertices in three thirds, etc.
            group_count = groups

            # Create the indices per group for this case
            indices_per_group: list[list[int]] = [[] for _ in range(group_count)]
            for vertex_index in range(vertices_numpy.shape[0]):
                group_index = vertex_index * group_count // vertices_numpy.shape[0]
                indices_per_group[group_index].append(vertex_index)
        elif isinstance(groups, list) and all(isinstance(int_value, int) for int_value in groups):

            raise NotImplementedError("List of group indices per vertex is not implemented yet")
        elif isinstance(groups, list) and all(isinstance(group, list) for group in groups) and all(isinstance(int_value, int) for int_list in groups for int_value in int_list):  # type: ignore[union-attr]
            raise NotImplementedError("List of lists of group indices per vertex is not implemented yet")
        else:
            raise NotImplementedError(f"Group buffer shape not supported: {type(groups)}")

        return group_count, indices_per_group
