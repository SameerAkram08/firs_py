class animal:
 def __init__(self, breed , name):
     self.breed= breed
     self.name= name


class cats (animal):

    def details(self):
        print ("name =",self.name)
        print ("breed name =",self.breed)

breed = input("Enter the breed of the cat: ")
name = input("Enter the name of the cat: ")  

a = cats(breed,name)
a.details()

