# Take input
N, K = input().split()
K = int(K)

# Convert to list to allow modification
N = list(N)

for i in range(len(N)):
    if K == 0:
        break

    if i == 0 and N[i] != "1":    # First digit can't be zero
        N[i] = "1"

        K -= 1                    # K is reduced by 1

    elif i > 0 and N[i] != "0":   # Other digit changed to 0
        N[i] = "0"

        K -= 1                    # K is reduced by 1

print("Min = ", ''.join(N))
   