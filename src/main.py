import numpy as np
import matplotlib.pyplot as plt
from helper import find_points


# Receive input from user

# input 3 points
# (wip) validasi titik harus berbeda

input_x_temp: str
input_y_temp: str
input_points: np.ndarray[np.ndarray[float]] = np.empty((3, 2), dtype=np.float32)

print("Enter 3 points")
for i in range(3):
    input_x_temp, input_y_temp = input(f"Point {i + 1} (x, y): ").split(",")
    input_points[i][0] = float(input_x_temp)
    input_points[i][1] = float(input_y_temp)

print()

# input iteration
# (wip) validasi iteration harus > 0

iteration: int = int(input("Enter iteration: "))

print()


# Finding points in bezier curve

bezier: np.ndarray[np.ndarray[float]] = find_points(input_points, 1, iteration)


# Testing plot

input_xs = [point[0] for point in input_points]
input_ys = [point[1] for point in input_points]
bezier_xs = [point[0] for point in bezier]
bezier_ys = [point[1] for point in bezier]

fig, ax = plt.subplots()
ax.scatter(input_xs, input_ys)
ax.plot(bezier_xs, bezier_ys)

plt.show()
