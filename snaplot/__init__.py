from .main import Camera
import matplotlib

# set non-interactive backend for Windows
matplotlib.use("Agg")

__version__ = "0.1.0"
__all__ = ["Camera"]
