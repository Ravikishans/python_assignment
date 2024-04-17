import sys
import shutil

def backup_files(source_dir, dest_dir):
    try:
        shutil.copytree(source_dir, dest_dir)
        print(f"Successfully backed up '{source_dir}' to '{dest_dir}'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_files(source_directory, destination_directory)
