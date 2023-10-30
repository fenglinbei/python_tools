import cv2

import numpy as np

from typing import Tuple

def pad2square(image: np.ndarray, size: int = None, pad: int = None) -> Tuple[np.ndarray, int, int, float]:
    h, w, c = image.shape
    
    if pad:
        a = pad * 2 + h if h >= w else pad * 2 + w
    else:
        a = h if h >= w else w
    
    pad_h = int((a - h) / 2)
    pad_w = int((a - w) / 2)
    
    new_image = np.zeros([a, a, c], dtype=np.float32)
    new_image[pad_h : pad_h + h, pad_w : pad_w + w] = image
    
    scale = 1
    if size:
        scale = size / a
        if scale > 1:
            new_image = cv2.resize(new_image, [size, size], interpolation=cv2.INTER_LINEAR_EXACT)
        else:
            new_image = cv2.resize(new_image, [size, size], interpolation=cv2.INTER_AREA)

        # pad_h, pad_w = int(pad_h * scale), int(pad_w * scale)
    
    return new_image, pad_h, pad_w, scale