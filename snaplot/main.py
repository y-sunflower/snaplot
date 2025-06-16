import os

import matplotlib.pyplot as plt
import matplotlib as mpl
from gifing import GIF

from typing import Union, Optional, Dict, Tuple, List


class Camera:
    """
    A class for capturing matplotlib figures and exporting them as a GIF.

    Attributes:
        verbose (bool): If True, prints log messages during execution.
        directory (str): Directory path where images are stored.
        n_images (int): Count of currently saved images.
        file_paths (list): List of saved image file paths.

    Args:
        force_new (bool): If True, clears the target directory before recording.
        dir_name (str): Subdirectory name inside ~/.snaplot to store images.
        verbose (bool): If True, enables logging of actions.
    """

    def __init__(
        self,
        force_new: bool = False,
        dir_name: str = "default",
        verbose: bool = True,
    ):
        self.verbose = verbose
        self.directory = os.path.join(os.path.expanduser("~"), ".snaplot", dir_name)

        if not os.path.exists(self.directory) or force_new:
            if self.verbose:
                print(f"Starting to record at {self.directory}")
            self.n_images = 0
            os.makedirs(self.directory, exist_ok=True)

            # clean up in case user wants to restart
            if force_new:
                for filename in os.listdir(self.directory):
                    file_path = os.path.join(self.directory, filename)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
        else:
            file_count = sum(
                1
                for entry in os.listdir(self.directory)
                if os.path.isfile(os.path.join(self.directory, entry))
            )
            self.n_images = file_count

    def snap(
        self,
        fig: Optional[mpl.figure.Figure] = None,
        extension: str = "png",
        **kwargs: Dict,
    ):
        """
        Capture and save a matplotlib figure to the recording directory.

        Args:
            fig (matplotlib.figure.Figure, optional): The figure to save. If None,
                uses the current active figure.
            extension (str): File extension/format to save the figure (e.g., 'png', 'jpg').
            **kwargs: Additional keyword arguments passed to `fig.savefig`.
        """
        self.extension = extension

        if fig is None:
            fig = plt.gcf()

        file_path = os.path.join(self.directory, f"{self.n_images}.{extension}")
        fig.savefig(fname=file_path, **kwargs)
        self.n_images += 1

        if self.verbose:
            print(f"Saving {file_path}")

    def stop(
        self,
        path: str,
        frame_duration: int = 100,
        n_repeat_last_frame: int = 1,
        resolution: Union[str, Tuple, List] = "auto",
    ):
        """
        Compile the saved images into a GIF.

        Args:
            path (str): Output path for the final GIF.
            frame_duration (int): Duration of each frame in milliseconds.
            n_repeat_last_frame (int): Number of times to repeat the last frame.
            resolution: An optional array with 2 integers (width and height, in
                pixels) for the resolution of the GIF. By default, it will use
                the dimensions of the last image in inches and convert them to pixels.
        """
        if resolution == "auto":
            fig = plt.gcf()
            width = fig.get_figwidth() * 96
            height = fig.get_figheight() * 96
        else:
            width = resolution[0]
            height = resolution[1]

        self.file_paths = list()
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                self.file_paths.append(file_path)

        if self.verbose:
            print(f"Saving {self.n_images} from {self.directory}")

        if len(self.file_paths) < 2:
            raise ValueError("Not enough images found (< 2).")

        gif = GIF(
            self.file_paths,
            frame_duration=frame_duration,
            n_repeat_last_frame=n_repeat_last_frame,
            verbose=self.verbose,
        )
        gif.set_size((width, height))
        gif.make(path)
