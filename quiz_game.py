print("Welcome to my computer quiz!")

playing = input("Do you want to play?")

if playing != "yes":
    quit()
    
print("Okay! Let's play :)")
score = 0


answer = input("What does CPU stand for?")
if answer == "central processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does GPU stand for?")
if answer == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does RAM stand for?")
if answer == "random access memory":
    print('correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does UNO stand for?")
if answer == "united nation organisation":
    print('correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does KIET stand for?")
if answer == "chutiya":
    print('correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does ansh stand for?")
if answer == "dudhiya":
    print('correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does anand stand for?")
if answer == "aalund":
    print('correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does rishu stand for?")
if answer == "coder":
    print('correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does Acer stand for?")
if answer == "aspire 7":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str( score ) + " questions correct!")



