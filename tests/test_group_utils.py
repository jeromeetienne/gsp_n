from gsp.utils.group_utils import GroupUtils


class TestGroupUtilsChecks:
    def test_is_instance_of_groups(self):

        # =============================================================================
        # True
        # =============================================================================
        assert GroupUtils.is_instance_of_groups(3) is True
        assert GroupUtils.is_instance_of_groups([0, 1, 2]) is True
        assert GroupUtils.is_instance_of_groups([[0, 1], [2, 3]]) is True

        # =============================================================================
        # False
        # =============================================================================
        assert GroupUtils.is_instance_of_groups("invalid") is False  # type: ignore
        assert GroupUtils.is_instance_of_groups([0, [1, 2]]) is False  # type: ignore
        assert GroupUtils.is_instance_of_groups([0, "invalid"]) is False  # type: ignore

        # TODO renable when the bug is fixed
        # assert GroupUtils.is_instance_of_groups([[0, 1], []]) is False
        # assert GroupUtils.is_instance_of_groups([[]]) is False


class TestGroupAsInt:
    def test_group_as_int(self):
        vertex_count = 6
        groups = 3
        expected_group_count = 3
        expected_indices_per_group = [[0, 1], [2, 3], [4, 5]]

        indices_per_group = GroupUtils.compute_indices_per_group(vertex_count, groups)
        group_count = len(indices_per_group)

        assert group_count == expected_group_count, f"group_count mismatch. Expected {expected_group_count}, got {group_count}"
        assert indices_per_group == expected_indices_per_group, f"indices_per_group mismatch. Expected {expected_indices_per_group}, got {indices_per_group}"

    def test_group_as_int_non_divisible(self):
        vertex_count = 7
        groups = 4
        expected_group_count = 4
        expected_indices_per_group = [[0, 1], [2, 3], [4, 5], [6]]

        indices_per_group = GroupUtils.compute_indices_per_group(vertex_count, groups)
        group_count = len(indices_per_group)

        assert group_count == expected_group_count, f"group_count mismatch. Expected {expected_group_count}, got {group_count}"
        assert indices_per_group == expected_indices_per_group, f"indices_per_group mismatch. Expected {expected_indices_per_group}, got {indices_per_group}"


class TestGroupAsListInt:
    def test_group_as_list_int(self):
        vertex_count = 6
        groups = [1, 3, 2]
        expected_group_count = 3
        expected_indices_per_group = [[0], [1, 2, 3], [4, 5]]

        indices_per_group = GroupUtils.compute_indices_per_group(vertex_count, groups)
        group_count = len(indices_per_group)

        assert group_count == expected_group_count, f"group_count mismatch. Expected {expected_group_count}, got {group_count}"
        assert indices_per_group == expected_indices_per_group, f"indices_per_group mismatch. Expected {expected_indices_per_group}, got {indices_per_group}"


class TestGroupAsListListInt:
    def test_group_as_list_list_int(self):
        vertex_count = 6
        groups = [[0], [1, 2, 3], [4, 5]]
        expected_group_count = 3
        expected_indices_per_group = [[0], [1, 2, 3], [4, 5]]

        indices_per_group = GroupUtils.compute_indices_per_group(vertex_count, groups)
        group_count = len(indices_per_group)

        assert group_count == expected_group_count, f"group_count mismatch. Expected {expected_group_count}, got {group_count}"
        assert indices_per_group == expected_indices_per_group, f"indices_per_group mismatch. Expected {expected_indices_per_group}, got {indices_per_group}"

    def test_group_as_list_list_int_non_contiguous(self):
        vertex_count = 6
        groups = [[0, 2], [1, 3, 5], [4]]
        expected_group_count = 3
        expected_indices_per_group = [[0, 2], [1, 3, 5], [4]]

        indices_per_group = GroupUtils.compute_indices_per_group(vertex_count, groups)
        group_count = len(indices_per_group)

        assert group_count == expected_group_count, f"group_count mismatch. Expected {expected_group_count}, got {group_count}"
        assert indices_per_group == expected_indices_per_group, f"indices_per_group mismatch. Expected {expected_indices_per_group}, got {indices_per_group}"
