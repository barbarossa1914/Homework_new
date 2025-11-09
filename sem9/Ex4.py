n = int(input())
arr1 = []
for i in range(n):
    arr = list(map(int, input().split()))
    for el in arr:
        b = (el, i)
        arr1.append(b)
arr1 = sorted(arr1, key=lambda x: x[0])
mrange = [0, 10**9]
nums = [k for k in range(n)]
arr2 = []
j = 0
for i in range(len(arr1)):
    try:
        while set(nums) != set(arr2):
            arr2.append(arr1[j][1])
            j += 1
    except:
        continue
    l = arr1[j-1][0] - arr1[i][0]
    if l < mrange[1]:
        mrange = [arr1[i], l]
    arr2 = arr2[1::]

print(str(mrange[0][0]) + '-' + str(mrange[0][0] + mrange[1]))