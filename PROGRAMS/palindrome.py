import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def check(a):

   return  a == a[::-1]
    

a = input("Enter a word you want to check: ")

if check (a):
    print ( a + " =" , a[::-1] ,"\nIts a Palindrome") 
    speaker.speak("Its a Palindrome")
 
else:
    print ( a + " =" ,a[::-1],"\nIts not a Palindrome") 
    speaker.speak("Its a not Palindrome")


