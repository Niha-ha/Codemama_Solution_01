Number = input().strip()

sum_of_digit = 0
for digit in Number:
    if digit.isdigit():
          sum_of_digit += int(digit)
if sum_of_digit % 2 == 0:
    print("Even")
else:
    print("Odd")