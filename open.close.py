file_input = open("read.txt",'r')
data = file_input.readline()
print(data)

file_input.open("read.txt",'w')
file_input.write("Python is amazing")
