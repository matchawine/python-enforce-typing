from .decorator import enforce_types

__version__ = "1.0.0.post1"


def get_version():
    """
    Returns a PEP 386-compliant version number from __version__.
    """
    return __version__
