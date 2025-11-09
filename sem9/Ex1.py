arr = list(map(int, input().split()))
n = len(arr)
out = 1
for i in range(0, n//2):
    if arr[i] < arr[2*i+1] and arr[i] < arr[2*i+2]:
        continue
    else:
        out = 0
        break
print(out)
