import os
import pathlib

# This script uses 'tesseract OCR capabalities to transform images showing some texts to
# .txt files. The aim of this script is to automate this transformation for many images (doing
# bulk OCR conversion).

# Requirement: You need to install tesseract package and its dependencies. To do that
# use the following command:
# sudo apt install tesseract-ocr tesseract-ocr-eng

# Before running the script You need to put all your images in the 'Input' folders.
# You will find all the generated .txt files in the 'Output' folder.

for path in pathlib.Path("Input").iterdir():
    if path.is_file():
        # Opening subtitles files
        print("************************************************")
        print(path.name)
        print(path)
        # Generate the .txt files
        command = f"tesseract {path}  {'./Output/'+path.name.strip('.jpeg')}"
        res = os.system(command)
        # the method returns the exit status

        print("Returned Value: ", res)
        # Deleting the last line in each generated .txt file
        with open('./Output/'+path.name.strip('.jpeg')+'.txt', 'r+') as file:
            # read an store all lines into list
            lines = file.readlines()
            # move file pointer to the beginning of a file
            file.seek(0)
            # truncate the file
            file.truncate()

            # start writing lines except the last line
            # lines[:-1] from line 0 to the second last line
            file.writelines(lines[:-1])
