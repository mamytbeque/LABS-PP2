import os
file_path = input("Enter the path of the file to delete: ")
def delete_file(path):
    if not os.path.exists(path):
        print("File does not exist.")
        return
    
    if not os.access(path, os.W_OK):
        print("Permission denied: You don't have the necessary permissions to delete this file.")
        return
    
    try:
        os.remove(path)
        print("File deleted successfully.")
    except OSError as e:
        print(f"Error deleting file: {e}")

file_path = input("Enter the path of the file to delete: ")

delete_file(file_path)
