text = "this has been overwritten\n new text\n code still works though"
with open ('test.txt', 'w') as file:
    file.write(text)

append    
text = "Hello \n my name is Gideon\n I'm 20"
with open('test.txt','a') as file:
    file.write(text)
 copy

import  shutil
shutil.copyfile('test.txt','copy.txt') 
