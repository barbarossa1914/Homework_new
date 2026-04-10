import math


r, a = list(map(int, input().split()))
l, s_c, s_s = 2 * math.pi * r, math.pi * r ** 2, a ** 2
print(f'Длина окружности равна {round(l, 2)}. \nПлощадь круга составляет {round(s_c/s_s*100, 2)} % от площади квадрата.')