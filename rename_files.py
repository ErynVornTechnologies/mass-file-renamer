import os

def rename_files():
    print("=== Mass File Renamer Script ===")
    folder_path = input("Enter the full path to the folder: ").strip()
    
    # Remove quotes if the user used "Copy as path" in Windows:
    if folder_path.startswith('"') and folder_path.endswith('"'):
        folder_path = folder_path[1:-1]
        
    base_name = input("Enter the new base name for the files (e.g., 'Holiday_Picture'): ").strip()
    
    if not os.path.isdir(folder_path):
        print(f"\nError: The path '{folder_path}' does not exist or is not a directory.")
        return

    # Get a list of files ignoring subdirectories
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    if not files:
        print("\nNo files found in the specified folder to rename.")
        return

    print(f"\nFound {len(files)} files. Starting to rename...")
    
    # Sort files alphabetically to keep their natural order before renaming
    files.sort()
    
    # Calculate how many zero-padding digits we need so that e.g. "10" comes correctly after "09"
    digits = len(str(len(files)))
    
    count = 1
    for filename in files:
        old_path = os.path.join(folder_path, filename)
        
        # Extract the original extension, e.g., ".jpg", ".txt"
        _, ext = os.path.splitext(filename)
        
        # New name format: "BaseName_01.extension"
        new_filename = f"{base_name}_{count:0{digits}d}{ext}"
        new_path = os.path.join(folder_path, new_filename)
        
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: '{filename}' -> '{new_filename}'")
            count += 1
        except Exception as e:
            print(f"Error renaming file '{filename}': {e}")
            
    print("\nFinished! All files have been renamed.")

if __name__ == "__main__":
    rename_files()
    input("\nPress Enter to exit the program...")