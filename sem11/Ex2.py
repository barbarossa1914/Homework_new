n = int(input())
arr = list(map(int, input().split()))
k = int(input())


def nod(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a = a % b
        a, b = b, a
    return a


def build_tree(a):
    tree = {}
    for i in range(n):
        tree[n+i] = a[i]
    for i in range(n-1, 0, -1):
        tree[i] = nod(tree[2*i], tree[2*i + 1])
    return tree


treee = build_tree(arr)


def max_tree(tree, left, right):
    left += n
    right += n
    _nod = 0
    while left < right:
        if (left & 1) > 0:
            _nod = nod(tree[left], _nod)
            left += 1
        if (right & 1) > 0:
            right -= 1
            _nod = max(tree[right], _nod)
        left = left // 2
        right = right // 2
    return _nod


out = []

for i in range(k):
    L, R = list(map(int, input().split()))
    out.append(max_tree(treee, L, R))

print(out, sep='\n')