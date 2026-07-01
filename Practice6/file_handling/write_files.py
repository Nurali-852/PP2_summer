with open("demofile.txt", "a") as f:    # "a"
  f.write("\nP.S Entered by Myrzaly Nurali") #appends right after last element. use \n to do newline. it also creates file by that name if other file does not exist

with open("demofile.txt") as f:
  print(f.read()) 

with open("demofile.txt", "w") as f:        # "w" overwrites  previous content. it also creates file by that name if other file does not exist
  f.write("Now its empty and filled with this content")


with open("demofile.txt") as f:
  print(f.read()) 

c = open("myfile.txt", "x")   # "x" creates empty file. error if named file already exists. 


