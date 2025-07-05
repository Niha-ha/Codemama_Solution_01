# Method 1 : direct input and sort
# N = int(input().strip())
# M = input().strip().split()

# M.sort(key= len)

# print(' '.join(M))

# Method 2 : using a function
def sort_string_by_len(N, M):
    if len(M) != N:
        raise ValueError()
    M.sort(key = len)
    return M

N = int(input().strip())
M = input().strip().split()

result = sort_string_by_len(N, M)
print(' '.join(result))