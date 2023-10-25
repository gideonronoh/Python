dev1 = ["Theo", 25, "Kotlin"]
dev2 = ["Myles",23, "PowerApps"]

class SoftwareDeveloper:
 alias = "wakuu"
 
 def __init__(self,name,age,language ):
  self.name= name
  self.age = age
  self.language=language

dev1 = SoftwareDeveloper ("Theo",25,"Kotlin")
dev2 = SoftwareDeveloper ("Myles",23,"PowerApps")
print(dev1.name,dev1.language)
print(dev2.name,dev2.language)  
print(SoftwareDeveloper.alias)

sel1 = ["Agume", 21, "Lead-Dev", ]
sel2 = ["Rono", 20, "Co-lead"]

class SoftwareEngineer:
    alias = "fine-bwoy"
    

    def __init__(self,name,age,position):
        self.name = name
        self.age = age
        self.position = position

se1 = SoftwareEngineer ("Agume","20","Lead-Dev")  
print(se1.name, se1.age)  
print(se1.alias)  
