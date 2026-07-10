#ignore
'''
import glob
import os
files = glob.glob(os.path.join(INPUT_FOLDER, "*_OMNIBUS_FINAL.csv"))
# Add this line immediately after to filter out any file starting with '._'
files = [f for f in files if not os.path.basename(f).startswith("._")]
'''



#delete
import os
def clean_appledouble_files(directory):
    """Deletes all macOS ._ hidden files in the given directory and subdirectories."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith("._"):
                try:
                    os.remove(os.path.join(root, file))
                except Exception:
                    pass
# Run this at the very beginning of your script
clean_appledouble_files("/Volumes/Extreme SSD/Documents/ucsf")



#no more via: copy in terminal (or in zsh/bash):
'''
export COPYFILE_DISABLE=1
'''




#manual clean
'''
dot_clean "/Volumes/Extreme SSD/Documents/ucsf"
'''