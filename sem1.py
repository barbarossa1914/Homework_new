'''Exercise 1
a = float()
b = float()
s = round(a+b, 5)
d = round(a - b, 5)
p = round(a*b, 5)
print(s, d, p, sep='\n')
'''


'''Exercise 2
n = int(123)
print(n%10)
'''


'''Exercise 3
numbers = str(input()).split()
av_g = 1
n = len(numbers)
for i in numbers:
    av_g *= float(i)
av_g = av_g**(1/n)
print(round(av_g, 5))
'''


'''Exercise 4
a = open("input.txt", 'r')
numbers = a.readline().replace('\n', '')
operation = a.readline().replace('\n', '')
a.close()
nums = numbers.split()
total = 0
if operation == '+':
    for i in nums:
        total += float(i)
if operation == '-':
    total = float(nums[0])
    for i in nums[1::]:
        total -= float(i)
if operation == '*':
    total = 1
    for i in nums:
        total *= float(i)
b = open('output.txt', 'w')
b.write(str(total))
b.close()
'''


'''Exercise 5
N = str(input())
b = int(input())
c = int(input())
n_len = len(N)
dec = 0
for i in range(n_len):
    dec += b**(n_len - i - 1) * int(N[i])
new_num = str()
while dec != 0:
    k = dec % c
    new_num += str(k)
    dec -= k
    dec = dec//c
print(int(new_num[::-1]))
'''



'''Exercise 6'''
import numpy as np
a = open("input.txt", 'r')
numbers = a.readline().replace('\n', '')
operation = a.readline().replace('\n', '')
base = int(a.readline().replace('\n', ''))
a.close()
nums = np.array(numbers.split())
def change_base_in(basa, number):
    n_len = len(number)
    dec = 0
    for i in range(n_len):
        dec += basa ** (n_len - i - 1) * int(number[i])
    return dec
vec_change_base_in = np.vectorize(change_base_in)
dec_nums = vec_change_base_in(base, nums)

total = 0
if operation == '+':
    for i in dec_nums:
        total += i
if operation == '-':
    total = dec_nums[0]
    for i in nums[1::]:
        total -= i
if operation == '*':
    total = 1
    for i in dec_nums:
        total *= i
new_num = str()
while total != 0:
    k = total % base
    new_num += str(k)
    total -= k
    total = total//base
new_num = int(new_num[::-1])

b = open('output.txt', 'w')
b.write(str(new_num))
b.close()



