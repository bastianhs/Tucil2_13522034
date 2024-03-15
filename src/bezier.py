import numpy as np


# find points in quadratic bezier curve with divide and conquer
def find_quad_bezier_dnc(
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

    # base case when we reach end of iteration
    if i == num_of_iter:
        return np.array((p0, r, p2))
    
    # find 1st half control points
    control_points1: np.ndarray[np.ndarray[float]] = np.array((p0, q0, r))

    # find 2nd half control points
    control_points2: np.ndarray[np.ndarray[float]] = np.array((r, q1, p2))
    
    # find bezier curve points from the 1st half and 2nd half
    bezier1: np.ndarray[np.ndarray[float]] = find_quad_bezier_dnc(control_points1, i + 1, num_of_iter)
    bezier2: np.ndarray[np.ndarray[float]] = find_quad_bezier_dnc(control_points2, i + 1, num_of_iter)

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
        num_of_iter: int
        ) -> np.ndarray[np.ndarray[float]]:

    mid_points: np.ndarray[np.ndarray[float]] = find_midpoints(control_points)
    
    # base case when we reach end of iteration
    if i == num_of_iter:
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
    bezier1: np.ndarray[np.ndarray[float]] = find_bezier_dnc(control_points1, i + 1, num_of_iter)
    bezier2: np.ndarray[np.ndarray[float]] = find_bezier_dnc(control_points2, i + 1, num_of_iter)

    # combine both result
    return np.concatenate((bezier1, bezier2))
