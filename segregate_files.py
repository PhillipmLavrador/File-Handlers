import os
import shutil

# Note we have to escape our backslashes here
path = "./Files/Negatives/"

for f in os.listdir(path):
    # Path to the original file
    original_file_path = os.path.join(path, f)
    # Only operate on files
    if os.path.isfile(original_file_path):
        # Get file name portion only
        file_name = os.path.basename(original_file_path)
        # Get the extension of the file and create a path for it
        extension = f.split(".")[-1]
        extension_path = os.path.join(path, extension)

        # Create the path for files with the extension if it doesn't exist
        if not os.path.exists(extension_path):
            os.makedirs(extension_path)

        # Copy the files into the new directory (copying is safer than moving, just so we can ensure it works as expected)
        shutil.move(original_file_path, os.path.join(extension_path, file_name))