import os

def clear_logs(path="/var/log"):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path):
                open(file_path, 'w').close()
        except Exception as e:
            print(f"Error: {e}")

clear_logs()
