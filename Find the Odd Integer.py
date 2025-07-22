# Function to fina an integer that appears odd numbers of times
def find_odd_integer(arr):

    # Loop through every single number in the array
    for num in set(arr):

        # Check if the count of the number is odd
        if arr.count(num) % 2 != 0:

            # Return the number if it appears odd numbers of times
            return num

# Read input from the user and convert it to list of integers
numbers = list(map(int, input().split()))

# Call the function with the input list
result = find_odd_integer(numbers)

# Print the output
print(result)
