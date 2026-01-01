n = int(input("Enter till how much numbers you want the sum!: "))
output = 0
for i in range(1, n+1):
    output += i
print(f"Sum of first {n} numbers is --> {output}")