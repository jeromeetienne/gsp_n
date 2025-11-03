from ..core.visual_base import VisualBase
from ..types.transbuf import TransBuf
from ..types.buffer import Buffer
from ..types.group import Groups


class Pixels(VisualBase):
    def __init__(self, positions: TransBuf, colors: TransBuf, groups: Groups):
        super().__init__()

        self._positions: TransBuf = positions
        self._colors: TransBuf = colors
        self._groups: Groups = groups

        self.check_attributes()

    # =============================================================================
    # get/set attributes
    # =============================================================================

    def get_positions(self) -> TransBuf:
        return self._positions

    def set_positions(self, positions: TransBuf) -> None:
        self._positions = positions
        self.check_attributes()

    def get_colors(self) -> TransBuf:
        return self._colors

    def set_colors(self, colors: TransBuf) -> None:
        self._colors = colors
        self.check_attributes()

    def get_groups(self) -> Groups:
        return self._groups

    def set_groups(self, groups: Groups) -> None:
        self._groups = groups
        self.check_attributes()

    def set_attributes(self, positions: TransBuf | None = None, colors: TransBuf | None = None, groups: Groups | None = None) -> None:
        """Set multiple attributes at once and then check their validity."""
        if positions is not None:
            self._positions = positions
        if colors is not None:
            self._colors = colors
        if groups is not None:
            self._groups = groups
        self.check_attributes()

    # =============================================================================
    # Sanity check functions
    # =============================================================================

    def check_attributes(self) -> None:
        """Check that the attributes are valid and consistent."""
        self.sanity_check_attributes(self._positions, self._colors, self._groups)

    @staticmethod
    def sanity_check_attributes_buffer(positions: Buffer, colors: Buffer, groups: Groups):
        """same as .sanity_check_attributes() but accept only Buffers.
        It is means to be used after converting TransBuf to Buffer.
        """
        # sanity check - each attribute must be a Buffer (not a transform chain)
        assert isinstance(positions, Buffer), "Positions must be a Buffer"
        assert isinstance(colors, Buffer), "Colors must be a Buffer"

        Pixels.sanity_check_attributes(positions, colors, groups)

    @staticmethod
    def sanity_check_attributes(positions: TransBuf, colors: TransBuf, groups: Groups):

        pass
