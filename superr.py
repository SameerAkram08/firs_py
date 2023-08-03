class Employee:
    def __init__(self,name,id):
     self.name= name
     self.id = id

class sameer(Employee):
    def __init__(self,name,id,dept):
     super().__init__(name,id)
     self.dept= dept

a = sameer("sam","22","it")
print(a.name,a.id,a.dept)     



