# 'В постфиксную'
'''
s = str(input())
q = []
num = ''
for i in range(len(s)):
    if s[i] in ['(', ')', '+', '-', '*', '/']:
        q.append(num)
        num = ''
        q.append(s[i])
    else:
        num += s[i]
q.append(num)
q = list(filter(lambda x: x != '', q))
i = 0
out = ''
stack = []


def p(o):
    if o == '*' or o == '/':
        return 1
    if o == '+' or o == '-':
        return 0
    return -1


for i in range(len(q)):
    if q[i] not in ['(', ')', '+', '-', '*', '/']:
        out += q[i] + ' '
    if q[i] == '(':
        stack.append(q[i])
    if q[i] in ['+', '-', '*', '/']:
        while stack and stack[-1] != '(' and p(stack[-1]) >= p(q[i]):
            out += stack[-1] + ' '
            stack.pop()
        stack.append(q[i])
    if q[i] == ')':
        while stack and stack[-1] != '(':
            out += stack[-1]
            stack.pop()
        if stack and stack[-1] == '(':
            stack.pop()
while stack:
    out += stack.pop() + ' '
print(out)

# 'В префиксную'

s = str(input())
q = []
num = ''
for i in range(len(s)):
    if s[i] in ['(', ')', '+', '-', '*', '/']:
        q.append(num)
        num = ''
        q.append(s[i])
    else:
        num += s[i]
q.append(num)
q = q[::-1]
for i in range(len(q)):
    if q[i] == '(':
        q[i] = ')'
    elif q[i] == ')':
        q[i] = '('
q = list(filter(lambda x: x != '', q))
i = 0
out = ''
stack = []


def p(o):
    if o == '*' or o == '/':
        return 1
    if o == '+' or o == '-':
        return 0
    return -1


for i in range(len(q)):
    if q[i] not in ['(', ')', '+', '-', '*', '/']:
        out += q[i] + ' '
    if q[i] == '(':
        stack.append(q[i])
    if q[i] in ['+', '-', '*', '/']:
        while stack and stack[-1] != '(' and p(stack[-1]) >= p(q[i]):
            out += stack[-1] + ' '
            stack.pop()
        stack.append(q[i])
    if q[i] == ')':
        while stack and stack[-1] != '(':
            out += stack[-1]
            stack.pop()
        if stack and stack[-1] == '(':
            stack.pop()
while stack:
    out += stack.pop() + ' '

print(out[::-1])
'''

# 'Ex4'
'''

class DS(list):
    def ins(self, item, position):
        p1 = self[0: position]
        p2 = self[position::]
        return p1 + [item] + p2


a = DS([1, 2, 3, 4, 6])
a = a.ins(5, 3)
print(a)
print(len(a))
print(a[3])
'''
# 'Ex2'
'''
q = input().split()
r = 0
q = list(filter(lambda x: x != '', q))
stack = []
try:
    for i in range(len(q)):
        if q[i] not in ['(', ')', '+', '-', '*', '/']:
            stack.append(q[i])
        if q[i] in ['(', ')', '+', '-', '*', '/']:
            if q[i] == '*':
                r = int(stack[-2]) * int(stack[-1])
            if q[i] == '/':
                r = int(stack[-2]) / int(stack[-1])
            if q[i] == '+':
                r = int(stack[-2]) + int(stack[-1])
            if q[i] == '-':
                r = int(stack[-2]) - int(stack[-1])
            stack.pop()
            stack.pop()
            stack.append(r)
            r = 0
except:
    print('Wrong expression')

print(stack[0])
'''
'Ex3'
s = str(input())
q = []
num = ''
for i in range(len(s)):
    if s[i] in ['(', ')', '+', '-', '*', '/']:
        q.append(num)
        num = ''
        q.append(s[i])
    else:
        num += s[i]
q.append(num)
q = list(filter(lambda x: x != '', q))
i = 0
out = ''
stack = []


def p(o):
    if o == '*' or o == '/':
        return 1
    if o == '+' or o == '-':
        return 0
    return -1


for i in range(len(q)):
    if q[i] not in ['(', ')', '+', '-', '*', '/']:
        out += q[i] + ' '
    if q[i] == '(':
        stack.append(q[i])
    if q[i] in ['+', '-', '*', '/']:
        while stack and stack[-1] != '(' and p(stack[-1]) >= p(q[i]):
            out += stack[-1] + ' '
            stack.pop()
        stack.append(q[i])
    if q[i] == ')':
        while stack and stack[-1] != '(':
            out += stack[-1]
            stack.pop()
        if stack and stack[-1] == '(':
            stack.pop()
while stack:
    out += stack.pop() + ' '
print(out)