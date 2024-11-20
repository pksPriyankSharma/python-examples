# example of a function adding two numbers
a = int(input('please enter 1st number to add : '))
b = int(input('please enter 2nd number to add : '))
def addTwoNum(a, b):
    sum = a + b
    return(sum)
result = addTwoNum(a,b)
print('Sum of the numbers is :', result)

