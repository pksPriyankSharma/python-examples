#strEx.py
firstName = "Meher" # variable of String type
print(firstName)
fullName = "Meher Krishna Patel"
print(fullName)

#input taken from user
score1 = input("Enter the value for Score 1: ")
score2 = input("Enter the value for Score 2: ")
messageString = "Total Score is %s"
totalScore = score1 + score2
print(messageString % totalScore)

messageInt = "Total Score in number is %s"
#score1 and score2 are stroed as String
#let's change these to integer
totalInt = int(score1) + int(score2)
print(messageInt % totalInt)



