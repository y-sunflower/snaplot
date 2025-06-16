import os

import matplotlib.pyplot as plt
import matplotlib as mpl
from gifing import GIF


class Camera:
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

    def snap(self, fig: mpl.figure.Figure = None, extension: str = "png", **kwargs):
        self.extension = extension

        if not hasattr(self, "file_paths"):
            self.file_paths = []

        if fig is None:
            fig = plt.gcf()

        file_path = os.path.join(self.directory, f"{self.n_images}.{extension}")
        self.file_paths.append(file_path)
        fig.savefig(fname=file_path, **kwargs)
        self.n_images += 1
        print(f"Saving {file_path}")

    def end(self, path, frame_duration=100, n_repeat_last_frame=1):
        print(self.file_paths)
        gif = GIF(
            self.file_paths,
            frame_duration=frame_duration,
            n_repeat_last_frame=n_repeat_last_frame,
            verbose=self.verbose,
        )
        gif.make(path)


if __name__ == "__main__":
    cam = Camera()

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 5], c="red", lw=1)
    ax.plot([3, 1, 3], [4, 2, 3], c="blue", lw=5)

    cam.snap()

    cam.end("here.gif")
