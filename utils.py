import os

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_output_path(output_folder):
    ensure_directory_exists("sentences")
    output_path = os.path.join("sentences", output_folder)
    ensure_directory_exists(output_path)
    return output_path
