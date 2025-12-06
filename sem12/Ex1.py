def decompose(n2):
    arr = []
    if n2 < 0:
        return 'number should be positive'
    if isinstance(n2, float):
        return 'number should be int-type'

    def dec(n, ll, i):
        if i <= n2//2 + 1:
            if n % i == 0:
                ll.append(i)
                n = n // i
            else:
                i += 1
            return dec(n, ll, i)

    dec(n2, arr, 2)
    if not arr:
        arr.append(n2)
    return arr


def test_decompose():
    assert decompose(10) == [2, 5], 'should be 2, 5'
    assert decompose(13) == [13], 'should be 13'
    assert decompose(1) == [1], 'should be 1'
    assert decompose(0) == [0], 'should be 0'
    assert decompose(-1) == 'number should be positive', \
        'number should be positive'
    assert decompose(1.2) == 'number should be int-type', \
        'number should be int-type'


test_decompose()
