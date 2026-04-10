s = input()

if len(s) >= 4:
    c = 0
    for i in range(4):
        if s[i] == s[i].upper():
            c += 1
    if c >= 3:
        print(s.upper())
    else:
        print(s)
else:
    print(s)