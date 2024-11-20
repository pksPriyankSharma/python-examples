# example of for loop using range function

print("print numbers in forward order")
for i in range(5):
    print(i+1, end=" ")
print('\nFinal value of i is', i)

print("print numbers in reverse order")
for j in range(5, 0, -1):
    print(j, end=" ")
print('\nFinal value of j is', j)


print('print list of fruits')
fruits=['apple', 'banana', 'orange']

for i in fruits:
    print(i, end=" ")
