# `snaplot`: record your plot process

`snaplot` is here to help your record your (matplotlib) plotting process, without having to think about it, and do things like:

![](docs/example.gif)

## Why

By nature, data visualization is an **iterative process**: no one creates the final, perfectly polished version of a graph on the first try. It always takes plenty of **trial and error**. And interestingly, visualizing this process can be quite insightful. That's where snaplot comes in.

<br><br>

## How to use

You run the following code as many time as needed to save all intermediate plots:

```python
import matplotlib.pyplot as plt
from snaplot import Camera

camera = Camera()

fig, ax = plt.subplots()
ax.plot([1,2,3], [1,2,3])

camera.snap()
```

And once you're done, you save it to a GIF:

```python
camera.stop("my_file.gif")
```

<br><br>

## Some cool things

- You can run `Camera()` multiple times without any issues. Unless you set `force_new=True`, it will automatically recognize that you're still recording.
- Even after calling `camera.stop("file.gif")`, you can keep recording. If you want to save the intermediate GIF, just use a different filename like `camera.stop("file2.gif")`.
- it (should) work with all the plotting packages based on matplotlib: matplotlib itself, seaborn, plotnine, yellowbrick, etc.
