n = int(input())
arr = list(map(int, input().split()))
k = int(input())


def build_tree(a):
    tree = {}
    for i in range(n):
        if a[i] != 0:
            tree[n + i] = 0
        else:
            tree[n + i] = 1
    for i in range(n-1, 0, -1):
        tree[i] = tree[2*i] + tree[2*i + 1]
    return tree


treee = build_tree(arr)


def max_tree(tree, left, right):
    left += n
    right += n
    _sum = 0
    while left < right:
        if (left & 1) > 0:
            _sum = tree[left] + _sum
            left += 1
        if (right & 1) > 0:
            right -= 1
            _sum = tree[right] + _sum
        left = left // 2
        right = right // 2
    return _sum


out = []

for i in range(k):
    L, R = list(map(int, input().split()))
    out.append(max_tree(treee, L, R))

print(out, sep='\n')