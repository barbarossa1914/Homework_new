s = input()

if len(s) <= 2:
    print(ord(s[0]))
elif 2 < len(s) < 10:
    print(ord(s[0]) + ord(s[-1]) + ord(s[(len(s) - 1) // 2]))
else:
    print(ord(s[-1]))