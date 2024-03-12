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
