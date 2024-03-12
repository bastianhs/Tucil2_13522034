import numpy as np


# Finding points in bezier curve
def find_points(
        control_points: np.ndarray[np.ndarray[float]], 
        i: int, 
        num_of_iter: int
        ) -> np.ndarray[np.ndarray[float]]:
    
    p0: np.ndarray[float] = control_points[0]
    p1: np.ndarray[float] = control_points[1]
    p2: np.ndarray[float] = control_points[2]
    q0: np.ndarray[float] = (p0 + p1) / 2
    q1: np.ndarray[float] = (p1 + p2) / 2
    r: np.ndarray[float] = (q0 + q1) / 2

    if i == num_of_iter:
        return np.array((p0, r, p2))
    
    control_points1: np.ndarray[np.ndarray[float]] = np.array((p0, q0, r))
    control_points2: np.ndarray[np.ndarray[float]] = np.array((r, q1, p2))
    bezier1: np.ndarray[np.ndarray[float]] = find_points(control_points1, i + 1, num_of_iter)
    bezier2: np.ndarray[np.ndarray[float]] = find_points(control_points2, i + 1, num_of_iter)
    return np.concatenate((bezier1, bezier2))
