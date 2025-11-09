n = int(input())
d = dict()
for i in range(n):
    film = str(input())
    try:
        d[film] += 1
    except:
        d[film] = 1
d = sorted(d.items(), key=lambda x: -x[1])
for el in d:
    print(el[0], el[1])
