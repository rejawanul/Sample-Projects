import os

def rename_files(folder_path, custom_name):
    # Get list of files in the folder
    files = os.listdir(folder_path)
    
    # Sort the files to maintain sequence
    files.sort()
    
    # Initialize sequence count
    sequence = 1
    
    # Iterate through each file
    for file in files:
        # Extract file extension
        name, extension = os.path.splitext(file)
        
        # Construct new filename
        new_name = f"Inv_{sequence}_{custom_name}{extension}"
        
        # Build full file paths
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        
        # Increment sequence count
        sequence += 1

# Example usage:
if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    custom_name = input("Enter the custom name: ")
    rename_files(folder_path, custom_name)
