'Ex1, 1.1, 1.2'
class Vector(object):
    def __init__(self, x, y, z):
        assert type(x) in [int, float]
        assert type(y) in [int, float]
        assert type(z) in [int, float]
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def scal_mul(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    def __abs__(self):
        return round((self.x**2 + self.y**2 + self.z**2)**0.5, 3)
    def __mul__(self, other):
        return Vector(self.x*other, self.y*other, self.z*other)
    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)
    def print_vector(self):
        print((self.x, self.y, self.z))
    def add_int(self, n):
        assert type(n) == int or n.type(float)
        return Vector(self.x + n, self.y + n, self.z + n)

a = Vector(1, 2, 10)
b = Vector(-1, -4, 1)
rad_v = [a, b]


def mass_center(arr):
    sigma = Vector(0, 0, 0)
    for el in arr:
        sigma = sigma + el
    return sigma * (1/len(arr))

mass_center(rad_v).print_vector()

def S(d1, d2, d3):
    v1 = d2-d1
    v2 = d3-d1
    iv = Vector(1, 0, 0)
    jv = Vector(0, 1, 0)
    kv = Vector(0, 0, 1)
    x1 = v1.x
    x2 = v2.x
    y1 = v1.y
    y2 = v2.y
    z1 = v1.z
    z2 = v2.z
    return abs((iv*y1*z2 + jv*z1*x2 + kv*x1*y2) - (kv*y1*x2 + iv*y2*z1 + jv*z2*x1))/2


o1 = Vector(1, 0, 0)
o2 = Vector(0, 0, 0)
o3 = Vector(0, 1, 0)
o4 = Vector(0, 0, 5)
o5 = Vector(2, 3, 1)

o = [o1, o2, o3, o4, o5]
m = 0
l = len(o)
for i in range(l):
    for j in range(l):
        for k in range(l):
            if S(o[i], o[j], o[k]) > m:
                m = S(o[i], o[j], o[k])
print(m)


