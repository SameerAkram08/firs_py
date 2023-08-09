a = input("Enter first string = ")
b = input("Enter second string = ")

def check():
    if len(a)!=len(b):
     print("it is not an ANAGRAM")

    else:
         if sorted(a) == sorted(b):
            print("It is an ANAGRAM")
         else:       
            print("it is not an ANAGRAM")

check()