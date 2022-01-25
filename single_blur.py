from motion_blur import motion_blur_image
import random
import cv2
import os

def single_blur():
    
    # Gets a list of all images
    images = (os.listdir("./Files/Selection/"))

    # Picks 5250 random images
    indexs = random.sample(range(10499), 5250)

    new_files = []

    for index in indexs:

        # Read the current image
        img = cv2.imread(f"./Files/Selection/{images[index]}")

        # Blur the image
        modified_image = motion_blur_image(img)

        # Make a copy of the image
        cv2.imwrite(f'./Files/BlurNegatives/{images[index]}', modified_image)

        new_files.append(f"./Files/Selection/{images[index]}")

    for file in new_files:
        
        # Delete every source image after blurring
        os.remove(file)

single_blur()