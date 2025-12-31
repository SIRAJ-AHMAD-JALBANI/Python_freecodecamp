obtained_marks = int(input("Enter Obtained Marks: "))

if 0 <= obtained_marks <= 100:
    if obtained_marks > 90:
        print("You got 'A+'")
    elif obtained_marks > 70:
        print("You got 'A' grade")
    elif obtained_marks > 60:
        print("You got 'B' grade")
    elif obtained_marks >= 33:
        print("You got 'C' grade")
    else:
        print("You are failed")
else:
    print("Invalid marks")
