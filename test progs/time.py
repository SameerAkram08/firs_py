import time

clock= time.strftime("%H::%M:%S")
print (" TIME -> ",clock)

name = input(("Enter your name = ")
 )
clock= int(time.strftime("%H"))

if (5 <= clock  < 12):
     print ("good morning",name.capitalize())


elif (12 <= clock  <= 16):
     print("good afternoon",name.capitalize())


elif (16 <= clock  <= 22 ):
     print("good evening",name.capitalize())

elif (clock <= 22):
    print("good night",name.capitalize())