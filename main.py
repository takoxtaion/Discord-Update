import os

def get_latest_file_in_downloads():

    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    
    files = [os.path.join(downloads_folder, f) for f in os.listdir(downloads_folder)]
    files = [f for f in files if os.path.isfile(f)]  
    
    if not files:
        print("No files found in Downloads folder.")
        return None
    
    latest_file = max(files, key=os.path.getmtime)
    
    print(f"Latest file found: {latest_file}")
    e
    command = f"sudo dpkg -i '{latest_file}'"
    print(f"Executing command: {command}")
    return os.system(command)

get_latest_file_in_downloads()
