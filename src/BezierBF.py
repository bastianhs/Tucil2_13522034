import numpy as np
import matplotlib.pyplot as plt


# find points in quadratic bezier curve with brute force
def find_quad_bezier_bf(
        control_points: np.ndarray[np.ndarray[float]],
        num_of_iterations: int
        ) -> np.ndarray[np.ndarray[float]]:
    
    p0: np.ndarray[float] = control_points[0]
    p1: np.ndarray[float] = control_points[1]
    p2: np.ndarray[float] = control_points[2]
    
    # find points in bezier curve
    bezier_points: np.ndarray[np.ndarray[float]] = np.empty((0, 2), dtype=np.float32)
    t: float
    for t in np.linspace(0, 1, num_of_iterations):
        bezier_point: np.ndarray[float] = (1 - t)**2 * p0 + 2 * (1 - t) * t * p1 + t**2 * p2
        bezier_points = np.append(bezier_points, np.array([bezier_point]), axis=0)
    
    return bezier_points


# visualize bezier curve with bruteforce for all iteration
def visualize_bezier_bf(
        input_points: np.ndarray[np.ndarray[float]],
        bezier: np.ndarray[np.ndarray[float]],
        ) -> None:
    
    xs_input: np.ndarray[float]
    ys_input: np.ndarray[float]
    xs_input, ys_input = input_points.transpose()
    
    xs_bezier: np.ndarray[float]
    ys_bezier: np.ndarray[float]
    xs_bezier, ys_bezier = bezier.transpose()

    for i in range(bezier.shape[0]):
        plt.clf()
        plt.title(f"Bezier Curve with Brute Force\nIteration {i + 1}")

        plt.scatter(xs_input, ys_input)
        plt.plot(xs_input, ys_input)
        
        plt.scatter(xs_bezier[:(i + 1)], ys_bezier[:(i + 1)])
        plt.plot(xs_bezier[:(i + 1)], ys_bezier[:(i + 1)])
        plt.pause(0.01)
