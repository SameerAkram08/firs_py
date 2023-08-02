class add:
    def __init__(self,a,b):
     self.a = a
     self.b = b
     self.sum =  a+b
class cont (add):
    def addition(self):
     print(self.sum)
a = add(10,11)
a.sum
print(a.sum)



# class add:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.sum = a + b

# class cont(add):
#     def print_sum(self):
#         print(self.sum)

# a = add(10, 11)

# print("Sum from 'add' class:", a.sum)  # Accessing sum directly from 'add' instance

# b = cont(10, 11)
# b.print_sum()  # Using the 'print_sum' method to print the sum from the 'cont' subclass




# program 3

# class Employee:
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id 

#   def showDetails(self):
#     print(f"The name of Employee: {self.id} is {self.name}")

# class Programmer(Employee):
#   def showLanguage(self):
#     print("The default langauge is Python")


# e1 = Employee("Rohan Das", 400)
# e1.showDetails()
# e2 = Programmer("Harry", 4100)
# e2.showDetails()
# e2.showLanguage()




