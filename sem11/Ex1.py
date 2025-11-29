n = int(input())
arr = list(map(int, input().split()))
k = int(input())


def build_tree(a):
    tree = {}
    for i in range(n):
        tree[n+i] = a[i]
    for i in range(n-1, 0, -1):
        tree[i] = max(tree[2*i], tree[2*i + 1])
    return tree


treee = build_tree(arr)


def max_tree(tree, left, right):
    left += n
    right += n
    m = 0
    while left < right:
        if (left & 1) > 0:
            m = max(tree[left], m)
            left += 1
        if (right & 1) > 0:
            right -= 1
            m = max(tree[right], m)
        left = left // 2
        right = right // 2
    return m


out = []

for i in range(k):
    L, R = list(map(int, input().split()))
    out.append(max_tree(treee, L, R))

print(out, sep='\n')
