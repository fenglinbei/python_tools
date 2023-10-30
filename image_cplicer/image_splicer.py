import cv2
import os

import numpy as np

from typing import List, Dict

image_dir = "./data/images/splice/"
save_dir = "./data/images/splice/output/"

def get_image_dict(image_dir: str) -> dict:
    image_file_list: List[str] = os.listdir(image_dir)

    image_dict = {}

    for image_file_name in image_file_list:
        if image_file_name.split(".")[-1] == "png":
            image_num = int(image_file_name.split(".")[0])
        else:
            continue
        image_path = os.path.join(image_dir, image_file_name)

        image_dict[image_num] = cv2.imread(image_path)
    
    return image_dict

def cut_image(image: np.ndarray) -> np.ndarray:
    output = image[258 : 748][:]
    return output

def splice_image(image_dict: Dict[int, np.ndarray]) -> np.ndarray:

    total_len = len(image_dict)
    print(list(image_dict.keys()))
    h, w, c = image_dict[0].shape

    expand = 1.5

    per_h = int(490 * expand)

    output_w = w
    output_h = total_len * per_h

    output = np.zeros([output_h, output_w, c])

    for i in range(total_len):
        image = image_dict[i]
        cuted_image = cut_image(image)

        output[per_h * i : per_h * (i + 1)][:] = cv2.resize(cuted_image, [w, per_h])

    return output

if __name__ == "__main__":
    image_dict = get_image_dict(image_dir)

    output = splice_image(image_dict)

    cv2.imwrite(os.path.join(save_dir, "output.png"), output)