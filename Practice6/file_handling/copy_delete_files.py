import os
# os.remove("demofile.txt")   # removes a file 

if os.path.exists("demofile.txt"):     #to avoid error if that file does not exist
  os.remove("demofile.txt")
else:
  print("The file does not exist") 

if os.path.exists("myfolder"):
 os.rmdir("myfolder")  # rmdir() removes folder. BUT ONLY EMPTY folders
else:
 print("The folder does not exist")                     

import shutil #used to copy file/folders

# Option 1: Copies file data and permissions (Recommended)
shutil.copy("source.txt", "destination.txt")

# Option 2: Copies file data, permissions, and metadata like timestamps
shutil.copy2("source.txt", "destination.txt")      

# Option 3: Copies an entire directory/folder recursively
#shutil.copytree("source_folder", "destination_folder")
with open("destination.txt") as f:
  print(f.read())