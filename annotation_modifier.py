import xml.etree.ElementTree as ET

def generate_xml(file):
        
    # Opens XML File
    mytree = ET.parse(f'./Files/Annotations/{file}')
    myroot = mytree.getroot()

    # Parses
    for filename in myroot.iter('filename'):
        old_name = filename.text
        
        # Edits the target image name
        filename.text = str(f"mb_{old_name}")
        
        # Saves with a new namek
        mytree.write(f"./Files/BlurAnnotations/mb_{file}")
