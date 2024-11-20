# the example captures the use of and logic, which means both of the conditions must be true

x = int(input("Please provide an input number to test:\t"))

if(x%2==0 and x%3==0):
    print("The number is divisible by 2 nad 3 both!")

elif(x%2==0):
    print("The number is divisible by 2 only")
elif(x%3==0):
    print("The number is divisible by 3 only")
else:
    print("The number is NOT divisible by 2 and 3 both")
    print("x%2= ",x%2)
    print("x%3= ",x%3)
print("Thank you for running the Script.")