from .main import Camera
import matplotlib

# set non-interactive backend for Windows
# https://github.com/y-sunflower/snaplot/issues/11
matplotlib.use("Agg")

__version__ = "0.2.0"
__all__ = ["Camera"]
