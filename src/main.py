import numpy as np
import matplotlib.pyplot as plt
import time
from bezier import find_quad_bezier_dnc


# receive input from user

# input number of points

while True:
    try:
        num_of_points: int = int(input("Enter number of points: "))
        if num_of_points > 0:
            print()
            break
        print("Number of points must be greater than 0.\n")
        
    except ValueError:
        print("Invalid input.\n")

# input coordinates 

input_x_temp: str
input_y_temp: str
input_points: np.ndarray[np.ndarray[float]] = np.empty((num_of_points, 2), dtype=np.float32)

while True:
    print(f"Enter {num_of_points} points")
    try:
        for i in range(num_of_points):
            input_x_temp, input_y_temp = input(f"Point {i + 1} (x, y): ").split(",")
            input_points[i][0] = float(input_x_temp)
            input_points[i][1] = float(input_y_temp)
        
        print()
        break
    except ValueError:
        print("Invalid input.\n")

# input iteration

while True:
    try:
        iteration: int = int(input("Enter iteration: "))
        if iteration > 0:
            print()
            break
        print("Iteration must be greater than 0.\n")

    except ValueError:
        print("Invalid input.\n")


# finding points in bezier curve

start: float = time.time()

bezier: np.ndarray[np.ndarray[float]] = find_quad_bezier_dnc(input_points, 1, iteration)

end: float = time.time()
print(f"Execution time: {(end - start) * 1000} ms\n")


# test plotting points and line

input_xs = [point[0] for point in input_points]
input_ys = [point[1] for point in input_points]
bezier_xs = [point[0] for point in bezier]
bezier_ys = [point[1] for point in bezier]

fig, ax = plt.subplots()

ax.scatter(input_xs, input_ys)
ax.plot(input_xs, input_ys)
for i, j in zip(input_xs, input_ys):
    plt.text(i + 0.2, j + 0.2, f"({i}, {j})")

ax.scatter(bezier_xs, bezier_ys)
ax.plot(bezier_xs, bezier_ys)

plt.show()
