
#: Excercise:3

# Create a program capable of displaying Questions to the user like KBC
# Use list data-type to store the questions and their correct answers
# Display the final amount the person takes home post game-play

name = input("What is your name?\n")

print("\nGood to have you",name,",Welcome to Kaun Banega Crorepati !\n")

print("Here is your first question \n", )

questions = ["What is capital of India? ", "Who won FIFA 2022? ","How many planets in Solar system? ", "What is value of g?"]

answers = ["delhi", "argentina","8","9.8"]

a = 1000
b = 2000
c = 3000
d = 4000

answers1 = input(questions[0])
if answers1.lower() == answers[0]:
    print("Correct answer. You have won", a, "INR\n")

    answer2 = input(questions[1])
    if answer2.lower() == answers[1]:
        print("Correct answer. You have won", b, "INR\n")

        answer3 = input(questions[2])
        if answer3.lower() == answers[2]:
            print("Correct answer. You have won", c, "INR\n")
            
            answer4 = input(questions[3])
            if answer4.lower() == answers[3]:
                print("Correct answer. You have won", d, "INR\n")
            else:
                print("Wrong answer.Your take home amount is",c,"INR\n")
        else:
            print("Wrong answer.Your take home amount is",b,"INR\n")
        
    else:
        print("Wrong answer.Your take home amount is",a,"INR\n")

else:
    print("Galat Jawab, Tumse na ho paai",0,"INR\n")
    
print("It was great playing with you",name)