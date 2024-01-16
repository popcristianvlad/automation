import os
import sys

def rename_files(collection_count):
    folder_path = os.path.join(os.getenv('USERPROFILE'), 'Downloads')  # Get the current working directory

    # List all entries (files and directories) in the specified directory
    all_entries = os.listdir(folder_path)

    # Filter out directories and keep only files
    files = [entry for entry in all_entries if os.path.isfile(os.path.join(folder_path, entry))]

    # # List all files in the current directory
    # files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Sort the files to ensure a consistent order
    files.sort()

    # Initialize counters for collection and image numbers
    image_count = 1

    # Iterate over each file and rename it
    for file_name in files:
        # Split the file name and extension
        file_name_no_ext, file_extension = os.path.splitext(file_name)

        # Create the new file name using the specified format
        new_name = f"collection-{str(collection_count).zfill(4)}-image-{str(image_count).zfill(4)}{file_extension}"

        # Build the full path for the file
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)

        # Increment image count, reset to 1 when it reaches 1000
        image_count += 1

    print("Files renamed successfully.")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <collection_count>")
        sys.exit(1)

    # Extract the collection_count from the command-line argument
    collection_count_param = int(sys.argv[1])

    # Call the function with the provided collection_count
    rename_files(collection_count_param)