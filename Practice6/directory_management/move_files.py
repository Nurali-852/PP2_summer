import shutil
from pathlib import Path

# Move a file into a directory
shutil.move("C:/test/demo.txt", "C:/test_recursive/")

# Move and rename the file at the same time
shutil.move("C:/test/demo.txt", "C:/test_recursive/new_name.txt")

source_dir = Path("path/to/source")
target_dir = Path("path/to/destination")

# Ensure the destination folder exists before moving
target_dir.mkdir(parents=True, exist_ok=True)

# Loop through and move all text (.txt) files
"""
for file_path in source_dir.glob("*.txt"):
    shutil.move(str(file_path), str(target_dir / file_path.name))
"""
with open("C:\test_recursive\demo.txt") as f:         # with closes file automatically itself. if without it, to close use f.close() 
    print( f.read()) 
