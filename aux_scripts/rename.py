import os

# Define the directory containing the images
train_dir = '../dataset/mask'

# Get a list of all files in the directory
files = os.listdir(train_dir)

# Sort the files to ensure consistent numbering (optional, in case ordering matters)
files.sort()

# Iterate over each file and rename it
for i, file in enumerate(files):
    # Construct the old file path
    old_file_path = os.path.join(train_dir, file)
    
    # Check if it's a file (not a subdirectory)
    if os.path.isfile(old_file_path):
        # Construct the new file name and path
        new_file_name = f"mask_{i}{os.path.splitext(file)[1]}"  # Keep the original file extension
        new_file_path = os.path.join(train_dir, new_file_name)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)

print("Renaming complete!")