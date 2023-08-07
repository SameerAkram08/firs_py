import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

list = ["Sameer" , "Akram","Ramsha"]

for name in list:
    speaker.Rate = 2  # Set the speech rate to be faster
    speaker.speak("Hello"+ name)


