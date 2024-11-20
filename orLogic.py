# example of OR logic, check divisibility by 2 and 3

x = int(input("Please provide an input number\t: "))

if(x%2==0 or x%3==0):
    print("The provided value is divisible by either 2 or 3")
    if(x%2==0 and x%3==0):
        print("The provided value is divisible by 2 nd 3 both!")
    elif(x%2==0):
        print("The value provided is divisible by 2 only")
    elif (x % 3 == 0):
        print("The value provided is divisible by 3 only")
else:
    print("x%2=", x % 2)
    print("x%3=", x%3)
print("Thank you.")