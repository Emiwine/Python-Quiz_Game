print("Welcome to my computer Quiz! ")

playing =  input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :) ")
score = 0
answer = input("What is CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Your answer is Correct!")
    score += 1
else:
    print("Incorrect!")
    
    

answer = input("What is GPU stands for? ")
if answer.lower() == "graphical processing unit":
    print("Your answer is correct! ")
    score += 1
else:
    print("Incorrect")


answer = input("What is RAM stands for? ")
if answer.lower() == "random access memory":
    print("Your answer is correct! ")
    score += 1
else:
    print("Incorrect")


answer = input("What is PSU stands for? ")
if answer.lower() == "power supply":
    print("Your answer is correct! ")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " question correct! ")
print("You got " + str((score/4) *100) + "%.")



