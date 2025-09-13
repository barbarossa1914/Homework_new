'Ex1'
'''
arr = str(input()).split()
l = int(arr[0])
arr = [int(arr[i]) for i in range(1, l)]
c = 0
for i in range(1, l + 1):
    try:
        arr.remove(i)
    except:
        c = i
print(c)
'''

'Ex12'
'''
n = int(input())
s = str(input())
s_new = str()
for i in range(0, len(s), n):
    s_new += s[i:n+i][::-1]
print(s_new)
'''


'Ex3'
'''
s = str(input())
ul = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']
ml1 = ['E', 'J', 'S', 'Z']
ml2 = ['3', 'L', '2', '5']

is_pal = s == s[::-1]
is_mir = 0
for i in range(len(s) - len(s)//2):
    if (s[i] == s[-i-1] and s[i] in ul) or (s[i] in ml1 and s[-i-1] in ml2 and ml1.index(s[i]) == ml2.index(s[-i-1])) or (s[i] in ml2 and s[-i-1] in ml1 and ml2.index(s[i]) == ml1.index(s[-i-1])):
        is_mir = 1
    else:
        is_mir = 0
        break
if is_pal and is_mir:
    print(f"{s} is a mirrored palindrome.")
elif is_pal and not is_mir:
    print(f'{s} is a regular palindrome.')
elif is_mir and not is_pal:
    print(f'{s} is a mirrored string.')
else:
    print(f'{s} is not a palindrome.')
'''

'Ex4'
'''
arr = str(input()).split()
for i in range(0, len(arr)-1, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
print(*arr, sep=' ')
'''

'Ex5'
'''
arr = str(input()).split()
arr1 = list(arr[-1])
arr1.extend(arr[0:len(arr)-1])
print(*arr1, sep=' ')
'''


'Ex6'
'''
arr = str(input()).split()
d = {}
for el in arr:
    am = arr.count(el)
    d.setdefault(am, []).append(el)
print(*d.get(1), sep=' ')
'''



'Ex7'
'''
arr = str(input()).split()
m = 0
m_el = str()
for el in arr:
    am = arr.count(el)
    if am > m:
        m_el = el
        m = am
print(m_el)
'''



'Ex8'
'''
n = int(input())
arr = str(input()).split()
l = len(arr)//2
k = 0
m = 0
for i in range(n):
    for j in range(n):
        if int(arr[i]) > int(arr[j]):
            k += 1.
    if k == l:
        m = arr[i]
        break
    else:
        k = 0
print(m)
'''


'Ex9'
'''
import re
with open('input.txt', 'r') as file:
    text = file.read()
    print(text)
    arr = re.findall(r'[^.?!]+[.?!]+', text)
    print(len(arr))
'''


'Ex10'
file = open('input.txt', 'r', encoding='utf-8')
text = file.read()
file.close()
l = len(text)
text = text + ' '
g = ['ё', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']
s = ['й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'ч', 'с', 'м', 'т', 'б', 'ь', 'ъ', ' ']
k = 0
n = 0
for i in range(l):
    try:
        if text[i+k-1] == ' ':
            n = 0
        elif text[i + k] in g and text[i + k - 1] in s and text[i + k - 1] != ' ':
            text = text[0:(i + k)] + text[(i + k)::].replace(text[i + k], text[i + k] + 'с' + text[i + k], 1)
            k += 2
    except:
        break

print(text[0:-1])
