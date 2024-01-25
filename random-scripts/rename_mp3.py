import os
from mutagen.mp3 import MP3

# Get the working directory (the Downloads directory)
working_dir = os.path.join(os.getenv('USERPROFILE'), 'Downloads')

# List all files in the working directory
files = os.listdir(working_dir)

# Filter .mp3 files
mp3_files = [file for file in files if file.endswith('.mp3')]

for mp3_file in mp3_files:
    file_path = os.path.join(working_dir, mp3_file)
    audio = MP3(file_path)
    
    # Extract metadata
    artist = audio.get('TPE1')  # Artist
    title = audio.get('TIT2')   # Title (Song name)

    # Construct new file name
    new_artist = artist[0] if artist else 'Unknown'
    new_title = title[0] if title else 'Unknown'
    
    # Replace '/' with ', '
    new_artist = new_artist.replace('/', ', ')
    new_title = new_title.replace('/', ', ')
    
    new_file_name = f"{new_artist} - {new_title}.mp3"
    
    # Rename the file
    if artist and title:
        new_file_path = os.path.join(working_dir, new_file_name)
        
        os.rename(file_path, new_file_path)
        print(f"Renamed {mp3_file} to {new_file_name}")
    else:
        print(f"Could not rename {mp3_file}. Missing metadata.")