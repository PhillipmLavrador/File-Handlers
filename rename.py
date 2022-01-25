import os
import string
import random
import xml.etree.ElementTree as ET

files = os.listdir("./Files/JPEGImages")

# print(files)


for file in files:

    already_taken = []

    new_name = (''.join(random.choices(string.ascii_uppercase + string.digits, k=30)))
    while new_name in already_taken:
        new_name = (''.join(random.choices(string.ascii_uppercase + string.digits, k=30)))

    already_taken.append(new_name)

    os.rename(f"./Files/JPEGImages/{file}", f"./Files/JPEGImages/{new_name}.jpg")

    mytree = ET.parse(f'./Files/Annotations/{file[:-4]}.xml')
    myroot = mytree.getroot()

    for filename in myroot.iter('filename'):
        old_name = filename.text
        
        # Edits the target image name
        filename.text = str(new_name)
        
        # Saves with a new namek
        mytree.write(f"./Files/Annotations/{new_name[:-4]}.xml")

        os.remove(f'./Files/Annotations/{file[:-4]}.xml')



