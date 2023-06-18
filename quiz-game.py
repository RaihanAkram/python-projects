print("\n\nWELCOME TO THE QUIZ GAME:")

play = input("\nDo you want to play? (yes/no): ").lower()

if play != "yes":
    quit()

count = 0

print("\n")

q1 = "Q1) Sample question 1 "
q2 = "Q2) Sample question 2 "
q3 = "Q3) Sample question 3 "
q4 = "Q4) Sample question 4 "
q5 = "Q5) Sample question 5 "
q6 = "Q6) Sample question 6 "
q7 = "Q7) Sample question 7 "
q8 = "Q8) Sample question 8 "

a1 = "a"
a2 = "b"
a3 = "c"
a4 = "d"
a5 = "e"
a6 = "f"
a7 = "g"
a8 = "h"


questions = [q1,q2,q3,q4,q5,q6,q7,q8]
answers = [a1,a2,a3,a4,a5,a6,a7,a8]

for i in range(0,8):
    questions[i] = input(questions[i])
    if questions[i].lower() == answers[i]:
        print("Correct!\n")
        count += 1
    else: 
        print("Not correct...")
        print("Correct answer is "+ answers[i] + "\n")

print("\nGAME OVER!\n")
print("Your score is " + str(count) + " / 8 ")
print("\nTHANKS FOR PLAYING!\n\n")


