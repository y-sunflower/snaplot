# `snaplot`: record your plot process

`snaplot` is here to help your record your (matplotlib) plotting process, without having to think about it, and do things like:

![](example.gif)

## Why

By nature, data visualization is an **iterative process**: no one creates the final, perfectly polished version of a graph on the first try. It always takes plenty of **trial and error**. And interestingly, visualizing this process can be quite insightful. That's where snaplot comes in.

## How to use

=== "1 - Create a camera"

    ```python
    import matplotlib.pyplot as plt
    from snaplot import Camera

    camera = Camera()
    ```

=== "2 - make a first plot"

    ```python
    plt.plot([1,2,3], [1,2,3])

    camera.snap()
    ```

=== "3 - a second one"

    ```python
    plt.plot([1,2,3], [1,2,3], color="red")

    camera.snap()
    ```

=== "4 - another one"

    ```python
    plt.plot([1,2,3], [1,2,3], color="red", lw=3)

    camera.snap()
    ```

=== "5 - Stop recording"

    ```python
    camera.stop("my_file.gif")
    ```

## All together

Highlighted lines are those that need to be modified to improve your graph iteratively:

```python hl_lines="6 7"
import matplotlib.pyplot as plt
from snaplot import Camera

camera = Camera()

fig, ax = plt.subplots()
ax.plot([1,2,3], [1,2,3])

camera.snap()

# Run this when you're done with your chart
# camera.stop("my_file.gif")
```

## Some cool things

- You can run `Camera()` multiple times without any issues. Unless you set `force_new=True`, it will automatically recognize that you're still recording.
- Even after calling `camera.stop("file.gif")`, you can keep recording. If you want to save the intermediate GIF, just use a different filename like `camera.stop("file2.gif")`.
