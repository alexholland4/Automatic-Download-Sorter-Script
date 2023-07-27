# Automatic Download Sorter Script

import os
import shutil


# helper function to get all the files in a given directory, and skip any folders 
def get_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):  # Check if the item is a file, not a directory.
            yield filepath


# helper function for moving files from one directory to another 
def move_files(source_directory, dest_directory, file):
    filename = file.split('\\')[1]
    print('Filename:', filename)
    source_path = source_directory + '/' + filename
    print('Source Path:', source_path)
    
    destination_path = dest_directory + '/' + filename
    print('Destination Path:', destination_path)
    try:
        shutil.move(source_path, destination_path)
        print(f"File moved successfully from '{source_path}' to '{destination_path}'.")
    except FileNotFoundError:
        print("Error: Source file not found.")
    except shutil.Error as e:
        print(f"Error: {e}")
    print()


while True:
    # Directory to move files from
    source_directory = ""  # CHANGE TO YOUR SOURCE DIRECTORY. I.E. C:/Users/username/Downloads

    #  Directories where files will end up
    pdf_directory = ""  # CHANGE TO YOUR PDF DESTINATION DIRECTORY. I.E. C:/Users/username/Documents/PDF Downloads
    pic_directory = ""  # CHANGE TO YOUR PDF DESTINATION DIRECTORY. I.E. C:/Users/username/Pictures/Saved Pictures

    # Loop through each file in target directory
    for file in get_files(source_directory):
        
        # PDF File move logic
        if file.endswith('.pdf'):
            print('PDF file found:', file)
            move_files(source_directory, pdf_directory, file)

        # PNG and JPG File move logic
        if ((file.endswith('.png')) or (file.endswith('.jpg')) or (file.endswith('.jpeg')) or (file.endswith('.JPG')) or (file.endswith('.PNG')) or (file.endswith('.JPEG'))):
            print('Image file found:', file)
            move_files(source_directory, pic_directory, file)
