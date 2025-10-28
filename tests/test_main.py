import pytest
import os
import matplotlib.pyplot as plt
from plotnine import ggplot, aes
import pandas as pd

import snaplot
from snaplot import Camera


@pytest.mark.parametrize("n_repeat_last_frame", [1, 20])
@pytest.mark.parametrize("frame_duration", [10, 200])
@pytest.mark.parametrize("extension", ["png", "jpg"])
@pytest.mark.parametrize("verbose", [True, False])
@pytest.mark.parametrize("record_id", [0, 2, "else"])
def test_snaplot_matplotlib(
    record_id, extension, frame_duration, n_repeat_last_frame, verbose
):
    camera = Camera.start(record_id=record_id, force_new=True, verbose=verbose)
    path = os.path.join(os.path.expanduser("~"), ".snaplot", f"record_{record_id}")
    assert os.path.exists(path)

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3])
    camera.snap(extension=extension)

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3], color="red")
    camera.snap(extension=extension, fig=fig)

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3], color="red", lw=3)
    camera.snap(extension=extension, fig=fig)

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3], color="red", lw=3)
    ax.spines["top"].set_visible(False)
    camera.snap(extension=extension, fig=fig)

    expected_files = {
        f"0.{extension}",
        f"1.{extension}",
        f"2.{extension}",
        f"3.{extension}",
    }
    actual_files = set(os.listdir(path))
    other_actual_files = set([os.path.basename(file) for file in camera.get_files()])
    assert actual_files == expected_files
    assert other_actual_files == expected_files

    path_output = os.path.join(
        os.path.expanduser("~"),
        ".snaplot",
        f"record_{record_id}",
        "here.gif",
    )
    camera.stop(
        path_output,
        frame_duration=frame_duration,
        n_repeat_last_frame=n_repeat_last_frame,
    )
    assert os.path.isfile(path_output)

    plt.close("all")


@pytest.mark.parametrize("n_repeat_last_frame", [1, 20])
@pytest.mark.parametrize("frame_duration", [10, 200])
@pytest.mark.parametrize("extension", ["png", "jpg"])
@pytest.mark.parametrize("verbose", [True, False])
@pytest.mark.parametrize("record_id", [0, 2, "else"])
def test_snaplot_plotnine(
    record_id, extension, frame_duration, n_repeat_last_frame, verbose
):
    camera = Camera.start(record_id=record_id, force_new=True, verbose=verbose)
    path = os.path.join(os.path.expanduser("~"), ".snaplot", f"record_{record_id}")
    assert os.path.exists(path)

    df = pd.DataFrame({"alpha": [1, 2, 3], "beta": [1, 2, 3], "gam ma": [1, 2, 3]})

    ggplot(df, aes(x="alpha", y="beta"))
    camera.snap(extension=extension)

    ggplot(df, aes(x="alpha", y="beta"))
    camera.snap(extension=extension)

    ggplot(df, aes(x="alpha", y="beta"))
    camera.snap(extension=extension)

    ggplot(df, aes(x="alpha", y="beta"))
    camera.snap(extension=extension)

    expected_files = {
        f"0.{extension}",
        f"1.{extension}",
        f"2.{extension}",
        f"3.{extension}",
    }
    actual_files = set(os.listdir(path))
    other_actual_files = set([os.path.basename(file) for file in camera.get_files()])
    assert actual_files == expected_files
    assert other_actual_files == expected_files

    path_output = os.path.join(
        os.path.expanduser("~"),
        ".snaplot",
        f"record_{record_id}",
        "here.gif",
    )
    camera.stop(
        path_output,
        frame_duration=frame_duration,
        n_repeat_last_frame=n_repeat_last_frame,
    )
    assert os.path.isfile(path_output)

    plt.close("all")


def test_version():
    assert snaplot.__version__ == "0.2.2"
