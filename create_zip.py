import os
import zipfile
import glob

def create_linux_compatible_zip(zip_name):
    # Files to include in the root
    root_patterns = ['*.html', '*.css', '*.js', '*.php', '*.json', '*.txt', '*.xml']
    files_to_add = []
    
    for pattern in root_patterns:
        files_to_add.extend(glob.glob(pattern))
        
    # Directories to include recursively
    dirs_to_add = ['assets', 'lib']
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add root files
        for file in files_to_add:
            # zipfile uses forward slashes internally for arcname if we specify it
            zipf.write(file, arcname=file)
            
        # Add directory contents
        for d in dirs_to_add:
            if os.path.exists(d):
                for root, _, files in os.walk(d):
                    for file in files:
                        file_path = os.path.join(root, file)
                        # Create the archive name with forward slashes for Linux compatibility
                        arcname = file_path.replace(os.sep, '/')
                        zipf.write(file_path, arcname=arcname)
                        
    print(f"Created {zip_name} successfully.")

if __name__ == "__main__":
    create_linux_compatible_zip("UrbanR8_Hostinger_Final_Linux.zip")
