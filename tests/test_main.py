import pytest
import os
import matplotlib.pyplot as plt

import snaplot
from snaplot import Camera


@pytest.mark.parametrize("n_repeat_last_frame", [1, 5, 20])
@pytest.mark.parametrize("frame_duration", [100, 10, 500])
@pytest.mark.parametrize("extension", ["png", "jpg", "jpeg"])
@pytest.mark.parametrize("dir_name", ["default", "something", "else"])
def test_create_dir(dir_name, extension, frame_duration, n_repeat_last_frame):
    cam = Camera.start(force_new=True, verbose=False, dir_name=dir_name)
    path = os.path.join(os.path.expanduser("~"), ".snaplot", dir_name)
    assert os.path.exists(path)

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3])

    cam.snap(extension=extension)
    cam.snap(extension=extension, fig=fig)
    cam.snap(extension=extension)

    expected_files = {f"0.{extension}", f"1.{extension}", f"2.{extension}"}
    actual_files = set(os.listdir(path))
    assert actual_files == expected_files

    path_output = os.path.join(
        os.path.expanduser("~"),
        ".snaplot",
        "here.gif",
    )
    cam.stop(
        path_output,
        frame_duration=frame_duration,
        n_repeat_last_frame=n_repeat_last_frame,
    )
    assert os.path.isfile(path_output)

    plt.close("all")


def test_version():
    assert snaplot.__version__ == "0.0.2"
