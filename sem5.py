'''
'Ex1'
import re
s = str(input())
nums = re.findall(r'student\d{3}', s)
mark = re.sub(r'student\d{3}', ' ', s[10::])
mark = mark.split()
nums = [int(el[len(el)-3:len(el)]) for el in nums]
mark = [int(el) for el in mark]
dic = {}
i = 0
for el in mark:
    try:
       dic[el] = [dic[el]] + [nums[i]]
    except:
        dic[el] = nums[i]
    i += 1
print(*dic[max(dic)], sep='-')
'''


'''
'Ex2'
import math
s = str(input()).split()
r, l = int(s[0]), int(s[-1])
Sr = math.pi*r**2
Sl = l**2
w = round(Sr/Sl * 100, 2)
d = round(2*math.pi*l, 2)
print(f'Длина окружности = {d}. Площадь круга составляет {w} % от площади квадрата.')
'''


'''
'Ex3'
s1 = input()
s2 = input()
def rev(a, b):
    if len(a) > 2:
        a = a[0:2][::-1] + a[2::]
    else:
        a = a[0:2][::-1]
    if len(b) > 2:
        b = b[0:2][::-1] + b[2::]
    else:
        b = b[0:2][::-1]
    return a+'-'+b
print(rev(s1, s2))
'''

'''
'Ex4'
def up(s):
    if len(s) >= 4:
        s = s.upper()
    else:
        pass
    return s

print(up('ruUu'))
'''

'''
'Ex5'
tag = str(input())
s = str(input())
tags = ['a', 'abbr', 'b', 'body', 'caption', 'cite', 'code', 'div', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'i', 's']
if tag in tags:
    print(f'<{tag}>{s}</{tag}>')
else:
    print('Введён неверный тег')
'''

'''
'Ex6'
s = str(input())
if len(s) <= 2:
    print(ord(s[0]))
elif 2 < len(s) <= 10:
    print(ord(s[0]) + ord(s[(len(s)-1)//2]) + ord(s[-1]))
else:
    print(ord(s[-1]))
'''