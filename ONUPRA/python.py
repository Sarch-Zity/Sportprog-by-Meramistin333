# Initialize an empty list
data = []

# Read input from a file
with open('input.txt', 'r') as file:
    # Read the first line to get values for 's' and 'n'
    s, n = map(int, file.readline().split())
    
    # Iterate through the next 'n' lines
    for i in range(n):
        x, d = map(int, file.readline().split())
        
        # Determine the open and close points based on conditions
        if x - d < 1:
            data.append([1, 0])  # open
        else:
            data.append([x - d, 0])  # open
        
        if x + d > s:
            data.append([s, 1])  # close
        else:
            data.append([x + d, 1])  # close

# Sort the data list
data.sort()

# Initialize variables
found_open = False
counter = 0
open_point = 1
excluded = 0

# Iterate through the sorted data
for i in range(len(data)):
    point = data[i]
    
    # Update the counter based on open and close points
    if point[1] == 0:
        counter += 1
    else:
        counter -= 1
    
    # Track the open and close points to calculate the excluded area
    if not found_open and counter > 0:
        open_point = point[0]
        found_open = True
    elif found_open and counter == 0:
        excluded += (point[0] - open_point) + 1
        found_open = False

# Write the result to an output file
with open('output.txt', 'w') as output_file:
    print(s - excluded, file=output_file)