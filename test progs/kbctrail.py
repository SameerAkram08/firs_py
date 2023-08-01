name = input("Whats your name = " )
print("hey welcome",name ,"to the game")

questions = ["what is the capital of pakistan","who is odi #1 batsman", "gaddafi stadium is located in which city"]
answers = ["islamabad","babar azam","lahore"]

a= 1000
b= 2000
c=3000

print(questions[0])
ans1 = input("Enter your answer = ",)
if (ans1 == answers[0]):
    print(f"correct answer you won {a} ")

    print(questions[1])
    ans2 = input("Enter your answer =  ")
    if (ans2 == answers[1]):
        print(f"correct answer you won {a+b} ")

        print(questions[2])
        ans3 = input("Enter your answer =  ")
        if (ans3 == answers[2]):
            print(f"correct answer you won {a+b+c} \n ")
            

        else :
            print(f"Wrong answer you take {a+b} ")
    else :
        print(f"Wrong answer you take {a} ")
else:
    print(f"Wrong answer you take {None} ")        
print("Congratulations you have completed the game ,Thanks for playing",name)    