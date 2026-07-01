import os


# List aka Print all entries in current directory
print (os.listdir())     # Output is ['create_list_dirs.py', 'move_files.py']. you can specify path to folder

# Create Directory

os.mkdir("c:/test")      

# Create Recursive directory 
os.makedirs("c:/test_recursive/w3school")    # parameter exist_ok=True to not raise Error. default value = False
