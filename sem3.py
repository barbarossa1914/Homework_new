

'''Ex4
size = int(input())
sim = str(input())
mask1 = [i for i in range(1, (size+1)//2 + 1)]
mask2 = [size//2 - i for i in range((size//2) + 1)]
mask1.extend(mask2)
for i in mask1:
    print(sim*i)
'''


'''Ex1
N = int(input()) - 1
def fib(num1, num2, num):
    if num != 0:
        num1, num2 = num1 + num2, num1
        num -= 1
        return fib(num1, num2, num)
    else:
        print(num1)
        return
try:
    fib(0,1, N)
except:
    print(0)
'''


'Ex2'
'''
N = int(input())
arr = []
def dec(n, l, i):
    if i <= N//2 + 1:
        if n % i == 0:
            l.append(i)
            n = n // i
        else:
            i += 1
        return dec(n, l, i)

dec(N, arr, 2)
if arr == []:
    arr.append(N)
print(arr)
'''


'''
a = int(input())
b = int(input())
arr1 = []
arr2 = []
def dec(n, l, i, ch):
    if i <= ch//2 + 1:
        if n % i == 0:
            l.append(i)
            n = n // i
        else:
            i += 1
        return dec(n, l, i, ch)

dec(a, arr1, 2, a)
if arr1 == []:
    arr1.append(a)
dec(b, arr2, 2, b)
if arr2 == []:
    arr1.append(b)
'''


'''
'Ex7'
import numpy as np
A = []
N = int(input())
M = int(input())
for i in range(N):
    A.append(str(input()).split())
A = np.array(A)
A = A.astype('int')
B = A[:, M-1]
A = np.delete(A, M-1, axis=1)
A_inv = np.linalg.inv(A)
X = A_inv@B
print(X)
'''


'''
'Ex6'
import numpy as np
A = []
'Enter the N pairs of x y separated with space'
N = int(input())
for i in range(N):
    A.append(str(input()).split())
A = np.array(A)
A = A.astype('int')
X = A[:, 0]
Y = A[:, 1]
def mnk(x, y):
    k = (np.mean(x*y) - np.mean(x)*np.mean(y))/(np.mean(x**2)-np.mean(x)**2)
    b = np.mean(y) - k*np.mean(x)
    print(k, b)
mnk(X, Y)
'''


'Ex8'
'''
import matplotlib.pyplot as plt
import numpy as np
import random

diap = int(input())
amount = int(input())
k = float(input())
sig = float(input())

X = np.linspace(0, diap, amount)
Y = k * X
Y_n = np.array([random.gauss(i, sig) for i in Y])

def mnk(x, y):
    k_m = (np.mean(x*y) - np.mean(x)*np.mean(y))/(np.mean(x**2)-np.mean(x)**2)
    b_m = np.mean(y) - k_m*np.mean(x)
    print(k_m, b_m)
    return k_m, b_m
a, b = mnk(X, Y_n)

plt.scatter(X, Y_n)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.plot(X, a * X + b, color='tab:red')

plt.xlabel('X')
plt.ylabel('Y')
plt.show()
'''


'''Ex5
import numpy as np

N = int(input())
M = int(input())
A = np.zeros((N, M))

def ulitka(mat, p, O, i):
    o_s = O.shape
    u_s = mat.shape
    mat[0, :] = np.arange(p, p + u_s[1])
    p = p + u_s[1]
    mat[1:, u_s[1] - 1] = np.arange(p, p + u_s[0] - 1)
    p = p + u_s[0] - 1
    mat = np.flip(mat, axis=1)
    mat[u_s[0] - 1, 1:] = np.arange(p, p + u_s[1] - 1)
    mat = np.flip(mat, axis=1)
    p = p + u_s[1] - 1
    mat = np.flip(mat, axis=0)
    mat[1:u_s[0] - 1, 0] = np.arange(p, p + u_s[0] - 2)
    mat = np.flip(mat, axis=0)
    p = p + u_s[0] - 2
    O[i:o_s[0]-i, i:o_s[1] - i] = mat
    i += 1
    if 0 in O:
        return ulitka(mat[1:u_s[0]-1, 1:u_s[1] - 1], p, O, i)
    else:
        print(O)5
        return
ulitka(A, 1, A, 0)
'''

'Ex 3'
s = str(input()).split()
A = int(s[0])
B = int(s[1])
def evk(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, d = evk(b, a % b)
        return y, x - y * (a // b), d

print(*evk(A, B), sep=' ')