# example of using elif logical block for more than one condition

x = int(input('please provide the input number:\t'))

if(x%2)==0:
    if(x%3)==0:
        print("The input number is divisible by 2 and 3 both!")
    else:
        print("The number is divisible by 2 only!")
        print("x%3=", x%3)
elif(x%3)==0:
    print("The number is divisible by 3 only!")
else:
    print("The number is not divisible by 2 nad 3!")
    print("x%3=", x % 3)
    print("x%2=", x % 2)
print("That was a nice example!")


