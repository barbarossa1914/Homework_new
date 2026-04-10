from collections import defaultdict


s = str(input())
i = 0
d = defaultdict()
while i < (len(s) - 11):
    j = i + 11
    b = str()
    while j < len(s) and s[j] != 's':
        b += s[j]
        j += 1
        d[int(s[i + 8 : i + 11])] = int(b)
    i = j

ans = []
max_b = max(d.values())
for el in d:
    if d[el] == max_b:
        ans.append(el)

print(*ans)

