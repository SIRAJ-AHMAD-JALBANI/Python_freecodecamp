def number_pattern(n):
    output = ""

    if not isinstance(n,int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    for n in range(1,n+1):
        output += str(n)+" "
    return output.rstrip()

print(number_pattern(4))