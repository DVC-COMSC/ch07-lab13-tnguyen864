# List to evaluate
numbers = [    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
               [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
               [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

# Number of rows
rnum = len(numbers)

# Number of columns
cnum = len(numbers[0])

# Variable to count cross shapes
isCross = 0

# Check for cross shapes
for i in range(rnum):
    for j in range(cnum):
        # If 1 is found
        if numbers[i][j] == 1:
            # Check for 1 above 1
            if numbers[i-1][j] == 1:
                # Check for 1 on left of 1
                if numbers[i][j-1] == 1:
                    # Check for 1 on right of 1
                    if numbers[i][j+1] == 1:
                        # Check for 1 under 1
                        if numbers[i+1][j] == 1:
                            # If all parameters met, count as cross shape
                            isCross += 1

# Print number of cross shapes in list
print(isCross)




