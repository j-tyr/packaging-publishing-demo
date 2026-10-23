from importlib.metadata import PackageNotFoundError, version as _pkg_version

try:
    __version__ = _pkg_version("packaging-publishing-demo-jt")
except PackageNotFoundError:
    # Not installed, e.g. imported straight from a source checkout
    __version__ = "0.0.0+unknown"


def greet(name: str = "world") -> str:
    """Return a greeting (placeholder functionality for the demo)."""
    return f"Hello, {name}! (packaging-publishing-demo-jt {__version__})"


def farewell(name: str = "world") -> str:
    """Return a farewell (placeholder functionality for the demo)."""
    return f"Goodbye, {name}! (packaging-publishing-demo-jt {__version__})"
