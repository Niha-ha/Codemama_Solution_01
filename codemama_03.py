N = int(input())            # Take integer input from the user
sum = 0                     # Initialize a variable to store the sum

for i in range(1, N + 1):   # Loop from 1 to N (inclusive)
    sum += i                # Add the current value of i to the sum

print(sum)                  # Output the final sum