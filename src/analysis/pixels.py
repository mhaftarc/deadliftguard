import json
import numpy as np

from pathlib import Path



def keypoints_to_pixels(points, width, height):

    result = np.array(points, dtype=float)  
    result[..., 0] *= width  
    result[..., 1] *= height  
    return result


def load_keypoints(stem):
    
    stem = Path(stem)
    keypoints = np.load(stem.parent / (stem.name + ".keypoints.npy"))
    with open(stem.parent / (stem.name + ".meta.json"), encoding="utf-8") as f:
        meta = json.load(f)

    if keypoints.ndim != 3 or keypoints.shape[1:] != (33, 4):
        raise ValueError
    
    if keypoints.shape[0] != meta["n_frames"]:
        raise ValueError
        
    return keypoints, meta