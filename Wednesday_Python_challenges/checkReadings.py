def checkReadings(n, readings):
    # Condition 1: No negative values
    for value in readings:
        if value < 0:
            return "INVALID"
    
    # Condition 2: At least one strict increase
    for i in range(1, n):
        if readings[i] > readings[i - 1]:
            return "VALID"
    
    return "INVALID"
