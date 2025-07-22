def find_odd_integer(arr):
    for num in set(arr):
        if arr.count(num) % 2 != 0:
            return num

numbers = list(map(int, input().split()))
result = find_odd_integer(numbers)
print(result)
