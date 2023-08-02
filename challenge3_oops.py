class Student:
    def __init__(self):
        self.nam = None
        self.roll = None

    def setname(self,name):
        self.nam = name
    
    def getname(self):
        return self.nam
    
    def setrollnos(self,rollnos):
        self.roll = rollnos
    
    def getrollnos(self):
        return self.roll

obj = Student()
obj.setname("Sudeep Kumar")
obj.setrollnos(12345)

print(obj.getname())        
print(obj.getrollnos()) 