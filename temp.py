import os

def mass_rename(directory, old_char, new_char):
    for filename in os.listdir(directory):
        if old_char in filename:
            new_filename = filename.replace(old_char, new_char)
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')

# Example usage
directory = 'path/to/your/directory'
old_char = 'old_char_to_replace'
new_char = 'new_char_to_replace_with'

mass_rename("data", "-", ".")
