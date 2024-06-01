import os
import shutil
from pathlib import Path

# Define the directory to organize
DIRECTORY_TO_ORGANIZE = '/path/to/your/directory'

# Define file type categories
FILE_TYPES = {
    'Documents': ['.pdf', '.docx', '.txt', '.doc', '.xlsx', '.xls'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.tar', '.gz', '.bz2', '.rar'],
    'Scripts': ['.py', '.js', '.sh', '.bat', '.ps1'],
    'Others': []
}

def create_folders(directory, file_types):
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)

def move_files(directory, file_types):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            file_extension = Path(item).suffix.lower()
            moved = False
            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    shutil.move(item_path, os.path.join(directory, folder, item))
                    moved = True
                    break
            if not moved:
                shutil.move(item_path, os.path.join(directory, 'Others', item))

def main():
    create_folders(DIRECTORY_TO_ORGANIZE, FILE_TYPES)
    move_files(DIRECTORY_TO_ORGANIZE, FILE_TYPES)
    print("Files have been organized successfully.")

if __name__ == "__main__":
    main()

