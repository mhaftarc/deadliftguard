import numpy as np


def angle(a, b, c):  # function to calculate the angle

    vec_a = np.asarray(a, dtype=float) - np.asarray(b, dtype=float)
    vec_c = np.asarray(c, dtype=float) - np.asarray(b, dtype=float)

    dot = np.dot(vec_a, vec_c)
    vector_length = np.linalg.norm(vec_a) * np.linalg.norm(vec_c)

    if vector_length == 0:
        return float('nan')  # return nan if either vector has zero length

    cosine = np.clip(dot / vector_length, -1.0, 1.0)
    return float(np.degrees(np.arccos(cosine)))






def trunk_angle(hip, shoulder):

    vec = np.asarray(shoulder, dtype=float) - np.asarray(hip, dtype=float)
    dx, dy = abs(vec[0]), abs(vec[1])

    if dx == 0 and dy == 0 :
        return float('nan')

    return float(np.degrees(np.arctan2(dx,dy)))