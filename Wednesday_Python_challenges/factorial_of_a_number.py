# Factorial of a Number
number = int(input("Enter a number: "))
output = 1
for i in range(1,number+1):
    output *= i
print(output)