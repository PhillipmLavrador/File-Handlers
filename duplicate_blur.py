from motion_blur import motion_blur_image
from annotation_modifier import generate_xml
import random
import cv2
import os


def duplicate_blur():

    # Lists all images
    images = (os.listdir("./Files/JPEGImages/"))

    # Picks 13365 random images out of the 46135 images
    indexs = random.sample(range(46134), 13365)

    for index in indexs:

        # Read Images
        img = cv2.imread(
            f"./Files/JPEGImages/{images[index]}"
            )

        # Blurs the image
        modified_image = motion_blur_image(img)

        # Saves a copy of the image
        cv2.imwrite(
            f'./Files/BlurJPEGImages/mb_{images[index]}', 
        modified_image)

        # Generates new annotation for the new blurred image
        generate_xml((f"{(images[index])[:-4]}.xml"))