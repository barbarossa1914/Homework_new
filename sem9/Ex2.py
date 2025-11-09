import random
arr1 = set(list(map(int, input().split())))
arr2 = set(list(map(int, input().split())))
arr3 = set(list(map(int, input().split())))
arr = list(arr2 & arr3 - arr1 & arr2 & arr3)


def quick_sort(l):
    n = len(l)
    if n == 1:
        return l
    elif n == 0:
        return []
    less = []
    more = []
    middle = []
    pivot = l[random.randint(0, n)]
    for el in l:
        if el < pivot:
            less.append(el)
        elif el > pivot:
            more.append(el)
        else:
            middle.append(el)
    return quick_sort(less) + middle + quick_sort(more)


print(quick_sort(arr))