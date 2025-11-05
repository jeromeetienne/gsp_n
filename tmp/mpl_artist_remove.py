import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# sleep 5 seconds to see the circle
import time

fig, ax = plt.subplots()

# Add an artist (e.g. a Circle)
circle = Circle((0.5, 0.5), 0.2, color="red")
ax.add_artist(circle)

plt.show(block=True)

print(f"before sleep")

# Later: remove the artist
circle.remove()

plt.show(block=True)

print(f"after sleep")


time.sleep(5)
