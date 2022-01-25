import os
import random
import shutil
import xml.etree.ElementTree as ET

# Lists every file in directory
labels = [
    file for file in os.listdir("Files/Negatives/")

    if os.path.isfile
        (os.path.join("Files/Negatives/", file))
    ]

# Pick 3000 numbers from 0 - 46241
indexs = random.sample(range(19242), 10500)

for index in indexs:    

    # Moves chosen files into new directory
    shutil.move(f"Files/Negatives/{labels[index]}", 
    f"Files/Selection/{labels[index]}")
    
