digit = input("Enter a number: ")

if digit.isdigit():
    print("Number of digits:", len(digit))
else:
    print("Invalid input! Please enter digits only.")
