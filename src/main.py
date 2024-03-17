import numpy as np
import matplotlib.pyplot as plt
import time
import os
from BezierDnC import find_quad_bezier_dnc, find_bezier_dnc, visualize_bezier_dnc
from BezierBF import find_quad_bezier_bf, visualize_bezier_bf


# receive input from user

# user choose to input points from file or terminal
while True:
    input_source: str = input("Do you want to input from file or terminal? (file/terminal)\n")
    if input_source in ["file", "terminal"]:
        print()
        break
    print("Invalid input.\n")

# read file
PARENT_FOLDER: str = "test/"
while input_source == "file":
    # input file name
    file_name: str = input("Enter file name (must be in test folder):\n")
    if not os.path.isfile(PARENT_FOLDER + file_name):
        print("File not found.\n")
        continue
    
    # read points from file
    try:
        with open(PARENT_FOLDER + file_name, "r") as file_input:
            input_points: np.ndarray[np.ndarray[float]] = np.empty((0, 2), dtype=np.float32)
            num_of_points: int = 0;
            while True:
                line: str = file_input.readline()
                if not line:
                    break
                x_temp: str
                y_temp: str
                x_temp, y_temp = line.split(",")
                input_point: np.ndarray[float] = np.array([[float(x_temp), float(y_temp)]])
                input_points = np.append(input_points, input_point, axis=0)
                num_of_points += 1
    
        if num_of_points > 1:
            print()
            break
        print("Number of points must be greater than 1.\n")
    except ValueError:
        print("Invalid point found in the file.\n")

# input number of points
while input_source == "terminal":
    try:
        num_of_points: int = int(input("Enter number of points: "))
        if num_of_points > 1:
            print()
            break
        print("Number of points must be greater than 1.\n")
        
    except ValueError:
        print("Invalid input.\n")

# input coordinates 
while input_source == "terminal":
    input_x_temp: str
    input_y_temp: str
    input_points: np.ndarray[np.ndarray[float]] = np.empty((num_of_points, 2), dtype=np.float32)
    print(f"Enter {num_of_points} points")
    try:
        for i in range(num_of_points):
            input_x_temp, input_y_temp = input(f"Point {i + 1} (x, y): ").split(",")
            input_points[i][0] = float(input_x_temp)
            input_points[i][1] = float(input_y_temp)
        
        print()
        break
    except ValueError:
        print("Invalid point.\n")

# user choose algorithm for finding bezier curve
algorithm: str = "divide and conquer"
while num_of_points == 3:
    print("Which algorithm do you want to use?")
    print("1. divide and conquer")
    print("2. brute force")
    algorithm = input("enter the number or name: ")
    if algorithm in ["1", "divide and conquer", "2", "brute force"]:
        print()
        break
    print("Invalid input.\n")

# input iteration
while True:
    try:
        num_of_iteration: int = int(input("Enter number of iteration: "))
        if num_of_iteration > 0:
            print()
            break
        print("Iteration must be greater than 0.\n")

    except ValueError:
        print("Invalid input.\n")

# user choose to visualize the result or not
visualize: str
while True:
    visualize = input("Do you want to visualize the result? (yes/no): ")
    if visualize in ["yes", "no"]:
        print()
        break
    print("Invalid input.\n")


# find points in bezier curve
start: float = time.time()

bezier: np.ndarray[np.ndarray[float]]
if num_of_points != 3:
    bezier = find_bezier_dnc(input_points, 1, num_of_iteration)
elif algorithm in ["1", "divide and conquer"]:
    bezier = find_quad_bezier_dnc(input_points, 1, num_of_iteration)
else:
    bezier = find_quad_bezier_bf(input_points, num_of_iteration)

end: float = time.time()
print(f"Execution time: {(end - start) * 1000} ms\n")


# plotting bezier curve result
if (visualize == "yes"):
    if algorithm in ["1", "divide and conquer"]:
        visualize_bezier_dnc(input_points, bezier, num_of_iteration)
    else:
        visualize_bezier_bf(input_points, bezier)
else:
    if algorithm in ["1", "divide and conquer"]:
        plt.title(f"Bezier Curve with Divide and Conquer")
    else:
        plt.title(f"Bezier Curve with Brute Force")
    
    xs_input: np.ndarray[float]
    ys_input: np.ndarray[float]
    xs_input, ys_input = input_points.transpose()
    plt.scatter(xs_input, ys_input)
    plt.plot(xs_input, ys_input)
    
    xs_bezier: np.ndarray[float]
    ys_bezier: np.ndarray[float]
    xs_bezier, ys_bezier = bezier.transpose()
    plt.scatter(xs_bezier, ys_bezier)
    plt.plot(xs_bezier, ys_bezier)

plt.show()
