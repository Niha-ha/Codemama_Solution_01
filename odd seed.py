
# Take input in one line
A, B = map(int, input().split())

# Initialize total
total = 0

# When First integer is less than second integer
if A < B:
    for num in range(A, B+1):
      if num % 2 != 0:
          total += num

# When First integer is greater than Second
elif A > B:
   for num in range(A, B-1, -1):
      if num % 2 != 0:
          total += num
else:
   pass


print(total)
