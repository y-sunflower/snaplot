::: snaplot.main.Camera

## Usage

```python
import matplotlib.pyplot as plt
from snaplot import Camera

camera = Camera.start()

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])  # first chart
camera.snap()

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 2, 3], color="red")  # second chart
camera.snap()

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 5, 3], color="green", lw=3)  # third chart
camera.snap()

fig, ax = plt.subplots()
ax.plot([5, 2, 4], [2, 3, 3], color="blue", lw=6)  # fourth chart
camera.snap()

camera.stop("my_file.gif", frame_duration=300)
```

![](my_file.gif)
