import random
import numpy as np
import cv2

def motion_blur_image(img):
    angle = random.random() * 180
    ang = (angle % 45) / 90 * np.pi
    size = int(random.random() * 17) + 1

    kernel = np.zeros((size, size))
    slope = np.arctan(ang)

    for x in range(size):
        kernel[x, int(x * slope)] = 1

    kernel = np.rot90(kernel, (angle // 45) * 2)

    # Normalize.
    kernel /= size

    # Apply the vertical kernel.
    mb = cv2.filter2D(img, -1, kernel)

    return mb




