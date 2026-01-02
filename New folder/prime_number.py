n = int(input())
if ( n > 2):
    for i in range(2,n):
        if(n % i == 0):
            print("NOT A PRIME NUMBER")
            break
        else:
            print("Prime number")
            break
elif n == 1:
    print("A prime number")
else:
    print("Not a valid number")