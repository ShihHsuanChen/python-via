try:
    from importlib.metadata import version
except (ImportError, ModuleNotFoundError):
    from importlib_metadata import version
try:
    __version__ = version(__name__)
except:
    __version__ = '0.0.0'

from . import app
from . import __main__
