import os

labels = (os.listdir("./Files/Annotations/"))
number = 0

delete_list = []

for label in labels:

    
    # print(f"./Files/Annotations/{label[:-4]}.jpg")

    if not os.path.isfile(f"./Files/JPEGImages/{label[:-4]}.jpg"):
        number += 1

        delete_list.append(label)

print(delete_list)
