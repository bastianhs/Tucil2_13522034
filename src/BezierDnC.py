import numpy as np
import matplotlib.pyplot as plt


# find points in quadratic bezier curve with divide and conquer
def find_quad_bezier_dnc(
        control_points: np.ndarray[np.ndarray[float]], 
        i: int, 
        num_of_iterations: int
        ) -> np.ndarray[np.ndarray[float]]:
    
    p0: np.ndarray[float] = control_points[0]
    p1: np.ndarray[float] = control_points[1]
    p2: np.ndarray[float] = control_points[2]
    q0: np.ndarray[float] = (p0 + p1) / 2
    q1: np.ndarray[float] = (p1 + p2) / 2
    r: np.ndarray[float] = (q0 + q1) / 2

    # base case when we reach end of iteration
    if i == num_of_iterations:
        return np.array((p0, r, p2))
    
    # find 1st half control points
    control_points1: np.ndarray[np.ndarray[float]] = np.array((p0, q0, r))

    # find 2nd half control points
    control_points2: np.ndarray[np.ndarray[float]] = np.array((r, q1, p2))
    
    # find bezier curve points from the 1st half and 2nd half
    bezier1: np.ndarray[np.ndarray[float]] = find_quad_bezier_dnc(control_points1, i + 1, num_of_iterations)
    bezier2: np.ndarray[np.ndarray[float]] = find_quad_bezier_dnc(control_points2, i + 1, num_of_iterations)

    # combine both result
    return np.concatenate((bezier1, bezier2))


# find midpoints for constructing general bezier curve
def find_midpoints(
        points: np.ndarray[np.ndarray[float]]
        ) -> np.ndarray[np.ndarray[np.ndarray[float]]]:
    
    mid_points: np.ndarray[np.ndarray[float]] = np.empty((0, 2), dtype=np.float32)
    for i in range(points.shape[0] - 1):
        mid_point: np.ndarray[float] = np.array([(points[i] + points[i+1]) / 2])
        mid_points = np.append(mid_points, mid_point, axis=0)
    
    # base case when there is only 1 midpoint result
    if mid_points.shape[0] == 1:
        return mid_points;
    
    mid_points2: np.ndarray[np.ndarray[float]] = find_midpoints(mid_points)
    return np.concatenate((mid_points, mid_points2))


# find points in general bezier curve with divide and conquer
def find_bezier_dnc(
        control_points: np.ndarray[np.ndarray[float]], 
        i: int, 
        num_of_iterations: int
        ) -> np.ndarray[np.ndarray[float]]:

    mid_points: np.ndarray[np.ndarray[float]] = find_midpoints(control_points)
    
    # base case when we reach end of iteration
    if i == num_of_iterations:
        return np.array((control_points[0], mid_points[-1], control_points[-1]))
    
    # find 1st half control points
    control_points1: np.ndarray[np.ndarray[float]] = np.array([control_points[0]])
    j: int
    k: int = 1
    for j in range(control_points.shape[0] - 1, 1, -1):
        mid_point: np.ndarray[np.ndarray[float]] = np.array([mid_points[k - 1]])
        control_points1 = np.append(control_points1, mid_point, axis=0)
        k += j
    
    mid_point: np.ndarray[np.ndarray[float]] = np.array([mid_points[k - 1]])
    control_points1 = np.append(control_points1, mid_point, axis=0)
    
    # find 2nd half control points
    control_points2: np.ndarray[np.ndarray[float]] = np.array(mid_point)
    for j in range(1, control_points.shape[0] - 1):
        k -= j
        mid_point: np.ndarray[np.ndarray[float]] = np.array([mid_points[k - 1]])
        control_points2 = np.append(control_points2, mid_point, axis=0)
    
    control_points2 = np.append(control_points2, np.array([control_points[-1]]), axis=0)
    
    # find bezier curve points from the 1st half and 2nd half
    bezier1: np.ndarray[np.ndarray[float]] = find_bezier_dnc(control_points1, i + 1, num_of_iterations)
    bezier2: np.ndarray[np.ndarray[float]] = find_bezier_dnc(control_points2, i + 1, num_of_iterations)

    # combine both result
    return np.concatenate((bezier1, bezier2))


# plot bezier curve with divide and conquer for each iteration
def plot_bezier_dnc_iteration(
        xs_bezier: np.ndarray[float],
        ys_bezier: np.ndarray[float],
        nth_iteration: int,
        ) -> None:

    xs_bezier_split: list[np.ndarray[float]]
    ys_bezier_split: list[np.ndarray[float]]
    xs_bezier_split = np.split(xs_bezier, 2 ** (nth_iteration - 1))
    ys_bezier_split = np.split(ys_bezier, 2 ** (nth_iteration - 1))
    
    colors: list[str] = ["red", "orange", "green", "blue", "purple"]
    plt.title(f"Bezier Curve with Divide and Conquer\nIteration {nth_iteration}")
    for i in range(len(xs_bezier_split)):
        xs: np.ndarray[float] = np.array((
            xs_bezier_split[i][0], 
            xs_bezier_split[i][xs_bezier_split[i].shape[0] // 2],
            xs_bezier_split[i][-1], 
        ))
        ys: np.ndarray[float] = np.array((
            ys_bezier_split[i][0], 
            ys_bezier_split[i][ys_bezier_split[i].shape[0] // 2],
            ys_bezier_split[i][-1], 
        ))
        plt.scatter(xs, ys, color=colors[nth_iteration % len(colors)])
        plt.plot(xs, ys, color=colors[nth_iteration % len(colors)])


# visualize bezier curve with divide and conquer for all iteration
def visualize_bezier_dnc(
        input_points: np.ndarray[np.ndarray[float]],
        bezier: np.ndarray[np.ndarray[float]],
        num_of_iterations: int
        ) -> None:
    
    xs_input: np.ndarray[float]
    ys_input: np.ndarray[float]
    xs_input, ys_input = input_points.transpose()
    
    xs_bezier: np.ndarray[float]
    ys_bezier: np.ndarray[float]
    xs_bezier, ys_bezier = bezier.transpose()
    
    for i in range(num_of_iterations):
        plt.clf()
        
        plt.scatter(xs_input, ys_input)
        plt.plot(xs_input, ys_input)
        plot_bezier_dnc_iteration(xs_bezier, ys_bezier, i + 1)
        
        plt.pause(1)
