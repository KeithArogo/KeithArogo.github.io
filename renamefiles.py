import os

def rename_files_in_folder(folder_path, prefix):
    # Get a sorted list of files in the folder
    files = sorted(os.listdir(folder_path))
    
    for i, filename in enumerate(files, start=1):
        # Check if the file already has the desired prefix and correct numbering
        if filename.startswith(prefix) and filename == f"{prefix}{i}.wav":
            continue  # Skip already correctly named files
        
        # Get the file extension (e.g., .wav)
        file_extension = os.path.splitext(filename)[1]
        # Construct the new filename
        new_name = f"{prefix}{i}{file_extension}"
        # Construct the full old and new file paths
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        
        # Debugging output
        print(f"Renaming: {old_file} to {new_file}")
        
        # Rename the file
        try:
            os.rename(old_file, new_file)
        except FileNotFoundError as e:
            print(f"Error renaming {old_file}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def rename_files_in_all_folders(base_path, prefix):
    for i in range(1, 5):
        folder_name = f"model{i}"
        folder_path = os.path.join(base_path, folder_name)
        rename_files_in_folder(folder_path, prefix)

# Set the base path to the current directory
base_path = os.path.dirname(os.path.abspath(__file__))
prefix = "sample"

rename_files_in_all_folders(base_path, prefix)
