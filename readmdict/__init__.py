"""Init."""
try:
    import lzo  # noqa
except ModuleNotFoundError:
    raise SystemExit(
        "\n\tPlease install python-lzo "
        " first. This packagewont work without lzo.")
from .readmdict import MDD, MDX

__version__ = "0.1.1"
VERSION = __version__.split(".")
__all__ = ("readmdict", "MDX", "MDD")
