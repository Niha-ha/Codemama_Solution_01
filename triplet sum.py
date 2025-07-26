def find_triplet(arr, p):
    N = len(arr)
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if arr[i] + arr[j] + arr[k] == P:
                    print(arr[i], arr[j], arr[k])
                    return

    print("No such triplet found")
                
# Input N
N = int(input())

# Input Array
arr = sorted(list(map(int, input().split())))

# Input target value P
P = int(input())

find_triplet(arr, P)
