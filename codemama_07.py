#Take input Number
N = int(input().strip())

#take array input
M = list(map(int, input().strip().split()))

#sorting M
M.sort()

is_consecutive = True

for i in range(N-1):
    if abs(M[i+1]-M[i]) != 1:
        is_consecutive = False
        break

if is_consecutive:
    print("true")
else:
    print("false")
    

    
    
              