import os
source = "mode.1"
destination = "C:\\Users\\GIDIE\\Desktop\\mode.1"

try:
  if os.path.exists(destination):
    print("already exists")
  else:
     os.replace(source,destination) 
     print(source + "was moved") 
except FileNotFoundError:
    print(source + "mode.1 not found")
