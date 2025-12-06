import numpy as np


def mnk(x, y):
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        return 'data should be a numpy array'
    if x.all() == 0:
        return 0, 0
    k = (np.mean(x*y) - np.mean(x)*np.mean(y))/(np.mean(x**2)-np.mean(x)**2)
    b = np.mean(y) - k*np.mean(x)
    return (k, b)


def test_mnk():
    assert mnk(np.array([1, 2, 3]), np.array([1, 2, 3])) == (1, 0),  \
        'should be 1, 0'
    assert mnk(np.array([-1, -2, -3]), np.array([1, 2, 3])) == (-1, 0), \
        'should be -1, 0'
    assert mnk(np.array([0, 0, 0]), np.array([0, 0, 0])) == (0, 0), \
        'should be 0, 0'
    assert mnk(3, 6) == 'data should be a numpy array'


test_mnk()
print(mnk(np.array([1, 2, 3]), np.array([1, 2, 3])))
print(mnk(3, 6))
