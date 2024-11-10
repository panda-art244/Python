from math import sqrt
def discriminant(a, b, c):
    return b ** 2 - 4 * a * c
def solve(a, b, c):
    d = discriminant(a, b, c)
    if d < 0:
        print(f'Корней нет')
    elif d == 0:
        print(f'Один корень, x = {- b / 2 / a}')
    else:
        print(f'Два корня, x1 = {(-b + sqrt(d)) / 2 / a}, x2 = {(-b - sqrt(d)) / 2 / a}')
solve(1, -1, 3)